from rest_framework import viewsets

from .serializers import ServiceSerializer, OrderSerializer
from ..models import Service, Order


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
