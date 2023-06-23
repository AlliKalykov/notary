from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaryViewSet, RateViewSet, PageViewSet, PageContentViewSet

router = DefaultRouter()
router.register("notary", NotaryViewSet)
router.register("rate", RateViewSet)
router.register("page", PageViewSet)
router.register("pagecontent", PageContentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
