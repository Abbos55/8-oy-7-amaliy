from rest_framework import serializers
from .models import Kategoriya, Vakansiya, Fikr


class VakansiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vakansiya
        fields = '__all__'


class VakansiyaMaoshSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vakansiya
        fields = ['maosh']


class KategoriyaQisqaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoriya
        fields = ['nomi']


class KategoriyaBatafsil(serializers.ModelSerializer):
    vakansiyalar = VakansiyaSerializer(many=True, read_only=True)

    class Meta:
        model = Kategoriya
        fields = ['id', 'nomi', 'davomiyligi', 'vakansiyalar']


class KategoriyaFaqatId(serializers.ModelSerializer):
    vakansiyalar = VakansiyaMaoshSerializer(many=True, read_only=True)

    class Meta:
        model = Kategoriya
        fields = ['id']


class FikrSerializer(serializers.ModelSerializer):
    muallif_nomi = serializers.CharField(source='muallif.username', read_only=True)

    class Meta:
        model = Fikr
        fields = ['id', 'muallif', 'muallif_nomi', 'matn', 'yaratilgan']
        read_only_fields = ['muallif', 'yaratilgan']
