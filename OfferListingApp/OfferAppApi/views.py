from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location, Store, Offer, User, Order, Payment, PaymentType
from . serializers import UserSerializer, LocationSerializer, StoreSerializer, OfferSerializer
from . serializers import PaymentSerializer, PaymentTypeSerializer, OrderSerializer


class UserList(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)

    def post(self):
        pass

    
class LocationList(APIView):

    def get(self, request):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class OfferList(APIView):

    def get(self, request):
        offer = Offer.objects.all()
        serializer = OfferSerializer(offer, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class StoreList(APIView):

    def get(self, request):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class PaymentList(APIView):

    def get(self, request):
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class PaymentTypeList(APIView):

    def get(self, request):
        payment_type = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(payment_type, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class OrderList(APIView):

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many = True)
        return Response(serializer.data)

    def post(self):
        pass
