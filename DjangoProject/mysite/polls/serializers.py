from random import choices

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from datetime import date
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

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Pole 'imie' powinno zawierać tylko litery!")
        return value

    def validate_nazwisko(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Pole 'nazwisko' powinno zawierać tylko litery!")
        return value

    def validate_data_dodania(self, value):
        if value > date.today():
            raise ValidationError("Data nie może być z przyszłości!")
        return value

class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'
        read_only_fields = ('id',)
