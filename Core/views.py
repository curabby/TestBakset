from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import VPSSerializer, VPSStatusUpdateSerializer
from .models import VPS

class VPSListCreateAPIView(APIView):
    '''
    1. Создание нового виртуального сервера.
    '''
    def post(self, request):
        serializer = VPSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrentVPSAPIView(APIView):
    '''
    2. Получение данных о конкретном сервере по его uid.
    '''
    def get(self, request, uid):
        server = get_object_or_404(VPS, uid=uid)
        serializer = VPSSerializer(server)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VPSListAPIView(APIView):
    """
    3. Вывод списка всех серверов с поддержкой фильтрации по заданным параметрам.
    """
    def get(self, request):
        #Фильтрация по параметрам
        filters = {}
        if 'status' in request.query_params:
            filters['status'] = request.query_params['status']
        if 'cpu' in request.query_params:
            filters['cpu'] = request.query_params['cpu']
        if 'ram' in request.query_params:
            filters['ram'] = request.query_params['ram']
        if 'hdd' in request.query_params:
            filters['hdd__gte'] = request.query_params['hdd']
        servers = VPS.objects.filter(**filters)
        serializer = VPSSerializer(servers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StatusVPSUpdateAPIView(APIView):
    '''
    4. Изменение статуса сервера (например, перевод в состояния started, blocked, stopped).
    '''
    def patch(self, request, uid):
        server = get_object_or_404(VPS, uid=uid)
        serializer = VPSStatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            server.status = serializer.validated_data['status']
            server.save()
            return Response({'message': 'Status updated successfully', 'status': server.status}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)