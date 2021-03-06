from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location, Store, Offer, User, Order, Payment, PaymentType
from . serializers import UserSerializer, LocationSerializer, StoreSerializer, OfferSerializer
from . serializers import PaymentSerializer, PaymentTypeSerializer, OrderSerializer


class UserList(APIView):

    @staticmethod
    def get(request):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)

    def post(self):
        pass

    
class LocationList(APIView):

    @staticmethod
    def get(request):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class OfferList(APIView):

    @staticmethod
    def get(request):
        offer = Offer.objects.all()
        serializer = OfferSerializer(offer, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class StoreList(APIView):

    @staticmethod
    def get(request):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class PaymentList(APIView):

    @staticmethod
    def get(request):
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class PaymentTypeList(APIView):

    @staticmethod
    def get(request):
        payment_type = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(payment_type, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class OrderList(APIView):

    @staticmethod
    def get(request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many = True)
        return Response(serializer.data)

    def post(self):
        pass
