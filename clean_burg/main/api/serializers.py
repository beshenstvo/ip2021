from rest_framework import serializers

from ..models import Service, Order, OrderItem


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "price", "price_currency", "created_at", "updated_at", ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["service", "price", "price_currency", ]
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "client_name", "client_phone", "client_comment", "items", "created_at", "updated_at", ]
