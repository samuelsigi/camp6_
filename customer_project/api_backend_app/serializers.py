import regex
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Customer, Order, OrderItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.RegexField(
        regex=r'^[a-zA-Z\s]*$',  # Allows only letters and spaces
        max_length=50,
        min_length=3,
        allow_blank=False,
        error_messages={
            'invalid': 'Name must contain only letters.',
            'max_length': 'Name must not exceed 50 characters.',
            'min_length': 'Name must be at least 3 characters long.'
        }
    )
    address = serializers.RegexField(
        regex=r'^[a-zA-Z0-9\s]*$',  # Allows letters, numbers, and spaces
        max_length=200,
        min_length=10,
        allow_blank=False,
        error_messages={
            'invalid': 'Address must contain only letters, numbers, and spaces.',
            'max_length': 'Address must not exceed 200 characters.',
            'min_length': 'Address must be at least 10 characters long.'
        }
    )

    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateField(format='%d/%m/%Y', input_formats=['%d/%m/%Y'])

    # customer = CustomerSerializer()
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    customer_details = CustomerSerializer(source='customer', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    order_details = OrderSerializer(source='order', read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        validated_data['item_name'] = validated_data['item_name'].upper()
        return super().create(validated_data)