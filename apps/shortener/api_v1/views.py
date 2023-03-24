from rest_framework.generics import CreateAPIView

from apps.shortener.models import Url

from .serializers import UrlModelSerializer


class UrlShortenerCreateAPIView(CreateAPIView):
    model = Url
    serializer_class = UrlModelSerializer

    def get_serializer_context(self) -> dict:
        """
        Pass request to the serializer
        """
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
