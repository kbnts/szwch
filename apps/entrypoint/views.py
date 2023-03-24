import logging

from django.conf import settings
from django.core.cache import cache
from django.http import Http404, HttpResponseRedirect
from django.views import View

from apps.shortener.models import Url

logger = logging.getLogger(__name__)


class EntrypointView(View):
    pk_url_kwarg = "url_id"

    async def get_url(self) -> str:
        """
        Get the target URL from the cache or database
        """
        if not (url_id := self.kwargs.get(self.pk_url_kwarg)):
            raise Http404()

        if url := cache.get(url_id):
            logger.info("URL found in cache: id=%s", url_id)
            return url

        try:
            url_obj = await Url.objects.aget(url_id=url_id)
        except Url.DoesNotExist:
            logger.warning("URL does not exist: id=%s", url_id)
            raise Http404()

        cache.set(url_id, url_obj.url, settings.URL_CACHE_EXPIRES_AFTER_SECS)
        return url_obj.url

    async def get(self, *args, **kwargs) -> HttpResponseRedirect:
        """
        Redirect to the target URL
        """
        url = await self.get_url()
        return HttpResponseRedirect(url)
