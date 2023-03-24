from rest_framework import serializers

from apps.shortener.models import Url


class UrlModelSerializer(serializers.ModelSerializer):
    short_url = serializers.HyperlinkedIdentityField(
        view_name="app:entrypoint",
        lookup_field="url_id",
        lookup_url_kwarg="url_id",
        read_only=True,
    )

    class Meta:
        model = Url
        fields = ["url", "short_url"]
        extra_kwargs = {
            "url": {"write_only": True},
        }
