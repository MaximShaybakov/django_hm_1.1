from django.db.models import Q
from urllib import request
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.serializers import AdvertisementSerializer
from .models import Advertisement
from rest_framework.filters import SearchFilter
from .permissions import IsOwnerOrReadOnly
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter] # DjangoFilterBackend, 
    filterset_class = AdvertisementFilter # works instead DjangoFilterBackend!!!
    filterset_fields = ['title', 'creator', 'created_at']
    search_fields = ['title', 'created_at']
    

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    # def get_queryset(self):
    #     filter_params = Q(status=self.request.user.objects)
    #     if self.request.user.is_authenticated:
    #         filter_params |= Q(creator=self.request.user)
    #     return Advertisement.objects.filter(filter_params)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
    
    