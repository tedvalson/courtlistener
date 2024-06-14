from rest_framework import viewsets

from cl.api.utils import LoggingMixin
from cl.audio.api_serializers import AudioSerializer
from cl.audio.filters import AudioFilter
from cl.audio.models import Audio


class AudioViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = AudioSerializer
    filterset_class = AudioFilter
    ordering_fields = (
        "id",
        "date_created",
        "date_modified",
        "date_blocked",
    )
    # Default cursor ordering key
    ordering = "-id"
    # Other cursor ordering keys
    other_cursor_ordering_keys = [
        "id",
        "date_created",
        "-date_created",
        "date_modified",
        "-date_modified",
    ]
    queryset = (
        Audio.objects.all()
        .select_related("docket")
        .prefetch_related("panel")
        .order_by("-id")
    )
