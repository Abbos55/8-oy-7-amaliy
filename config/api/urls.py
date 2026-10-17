from rest_framework.routers import DefaultRouter
from .views import (
    VakansiyalarViewSet,
    KategoriyaViewSet,
    FikrlarViewSet,
    KategoriyaVakansiyalarViewSet,
    KategoriyaDetailViewSet,
)

router = DefaultRouter()
router.register('vakansiyalar', VakansiyalarViewSet, basename='vakansiya-list')
router.register('kategoriyalar', KategoriyaViewSet, basename='kategoriya-list')
router.register('fikrlar', FikrlarViewSet, basename='fikr-list')
router.register('kategoriya-vakansiyalar', KategoriyaVakansiyalarViewSet, basename='kat-vak')
router.register('kategoriya-detail', KategoriyaDetailViewSet, basename='kat-detail')

urlpatterns = router.urls
