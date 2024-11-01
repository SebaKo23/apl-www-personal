from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoModelSerializer

class OsobaDetail(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = OsobaSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = OsobaSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OsobaList(APIView):
    def get(self, request):
        obj = Osoba.objects.all()
        serializer = OsobaSerializer(obj, many=True)
        return Response(serializer.data)

class OsobaSearch(APIView):
    def get(self, request):
        imie = request.query_params.get('imie', None)
        if imie:
            osoby = Osoba.objects.filter(imie=imie)
        else:
            osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

class StanowiskoDetail(APIView):
    def get_object(self, pk):
        try:
            return Stanowisko.objects.get(pk=pk)
        except Stanowisko.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = StanowiskoModelSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = StanowiskoModelSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StanowiskoList(APIView):
    def get(self, request):
        queryset = Stanowisko.objects.all()
        serializer = StanowiskoModelSerializer(queryset, many=True)
        return Response(serializer.data)
