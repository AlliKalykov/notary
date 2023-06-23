from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions
from account.permissions import IsAdmin, IsAccountOwner
from .models import Notary, Rate, Page, PageContent
from .serializers import NotarySerializer, RateSerializer, PageSerializer, PageContentSerializer


@extend_schema(
    tags=["notary"],
    summary="API для нотариусов",
    description="Получение списка нотариусов, создание, редактирование и удаление нотариусов",
)
class NotaryViewSet(viewsets.ModelViewSet):
    queryset = Notary.objects.all()
    serializer_class = NotarySerializer
    permission_classes = [IsAdmin | IsAccountOwner ]


@extend_schema(
    tags=["rate"],
    summary="API для отзывов",
    description="Получение списка отзывов, создание, редактирование и удаление отзывов",
)
class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(
    tags=["page"],
    summary="API для страниц",
    description="Получение списка страниц, создание, редактирование и удаление страниц",
)
class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAdmin, ]


@extend_schema(
    tags=["pagecontent"],
    summary="API для контента страниц",
    description="Получение списка контента страниц, создание, редактирование и удаление контента страниц",
)
class PageContentViewSet(viewsets.ModelViewSet):
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer
    permission_classes = [IsAdmin, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
