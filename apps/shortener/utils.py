from django.conf import settings


def get_url_id(url_instance) -> str:
    """
    Generates a unique short hash based on PK
    """
    return settings.HASHIDS_GENERATOR.encode(url_instance.id)
