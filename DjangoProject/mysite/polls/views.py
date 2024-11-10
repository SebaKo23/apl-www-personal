from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoModelSerializer

@api_view(['GET'])
def osoba_detail(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_update(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_delete(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def osoba_list(request):
    if request.method == 'GET':
        osoba = Osoba.objects.filter(wlasciciel=request.user)
        serializer = OsobaSerializer(osoba, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def osoba_search(request):
    imie = request.query_params.get('imie', None)
    if imie:
        osoby = Osoba.objects.filter(imie=imie)
    else:
        osoby = Osoba.objects.all()
    serializer = OsobaSerializer(osoby, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StanowiskoModelSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StanowiskoModelSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def stanowisko_list(request):
    if request.method == 'GET':
        stanowisko = Stanowisko.objects.all()
        serializer = StanowiskoModelSerializer(stanowisko, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_members(request, stanowisko_id):
    try:
        stanowisko = Stanowisko.objects.get(pk=stanowisko_id)
    except Stanowisko.DoesNotExist:
        return Response({"error": "Stanowisko not found"}, status=status.HTTP_404_NOT_FOUND)

    osoby = Osoba.objects.filter(stanowisko=stanowisko)
    serializer = OsobaSerializer(osoby, many=True)
    return Response(serializer.data)