from random import choices

from rest_framework import serializers
from .models import Osoba, Stanowisko

class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    plec = serializers.ChoiceField(choices=Osoba.Plec.choices)
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())
    data_dodania = serializers.DateField(required=True)

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        stanowisko_data = validated_data.get('stanowisko')
        instance.stanowisko = Stanowisko.objects.get(nazwa=stanowisko_data['nazwa'])
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.save()
        return instance

class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'
        read_only_fields = ('id',)
