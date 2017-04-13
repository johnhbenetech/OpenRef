from rest_framework import viewsets
from rest_framework import permissions
from core.permissions import IsOwnerOrReadOnly
from .models import Update, Provider
from .serializers import UpdateSerializer, ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

class UpdateViewSet(viewsets.ModelViewSet):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer