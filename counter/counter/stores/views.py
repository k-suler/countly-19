from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Store, Event
from .permissions import ReadOnly
from .serializers import StoreSerializer, EventSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (ReadOnly,)

    def get_permissions(self):
        permission_classes = []
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes.append(IsAdminUser)
        return [permission() for permission in permission_classes]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes.append(IsAdminUser)
        return [permission() for permission in permission_classes]
