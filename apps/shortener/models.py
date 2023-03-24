from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shortener.utils import get_url_id


class Url(models.Model):
    created_timestamp = models.DateTimeField(
        verbose_name=_("Created timestamp"), auto_now_add=True
    )
    url = models.URLField(verbose_name=_("URL"))
    url_id = models.CharField(verbose_name=_("Short URL"), max_length=15, default="")

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.pk and not self.url_id:
            # Generate a unique ID based on the PK
            self.url_id = get_url_id(self)
            super().save(update_fields=["url_id"])

    def __str__(self) -> str:
        return f"{self.url_id} - {self.created_timestamp:%Y-%m-%d %H:%M}"

    class Meta:
        verbose_name = _("Url")
        verbose_name_plural = _("Urls")
        ordering = [
            "-created_timestamp",
        ]
        indexes = [
            models.Index(
                fields=[
                    "url_id",
                ]
            )
        ]
