from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Vakansiya, Kategoriya, Fikr
from .serializers import (
    VakansiyaSerializer,
    KategoriyaBatafsil,
    KategoriyaFaqatId,
    FikrSerializer,
)


class VakansiyalarViewSet(ModelViewSet):
    queryset = Vakansiya.objects.all()
    serializer_class = VakansiyaSerializer


class KategoriyaViewSet(ModelViewSet):
    queryset = Kategoriya.objects.all()
    serializer_class = KategoriyaFaqatId


class FikrlarViewSet(ModelViewSet):
    queryset = Fikr.objects.all()
    serializer_class = FikrSerializer


class KategoriyaVakansiyalarViewSet(ModelViewSet):
    queryset = Kategoriya.objects.all()
    serializer_class = KategoriyaBatafsil


class KategoriyaDetailViewSet(ReadOnlyModelViewSet):
    queryset = Kategoriya.objects.all()
    serializer_class = KategoriyaFaqatId

    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return KategoriyaFaqatId
        return VakansiyaSerializer
