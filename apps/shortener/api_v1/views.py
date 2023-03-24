from rest_framework.generics import CreateAPIView

from apps.shortener.models import Url

from .serializers import UrlModelSerializer


class UrlShortenerCreateAPIView(CreateAPIView):
    """
    Converts the link to a shorter version
    """

    model = Url
    serializer_class = UrlModelSerializer
