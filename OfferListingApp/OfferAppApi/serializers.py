from rest_framework import serializers
from .models import Location, Store, Offer, User, Order, Payment, PaymentType


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User     
        fields = '__all__'  


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location     
        fields = '__all__'  


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store    
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer    
        fields = '__all__'  


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order    
        fields = '__all__'  


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment    
        fields = '__all__'  


class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentType
        fields = '__all__'  
