from django.shortcuts import render
from .serializers import *
from rest_framework.generics import *
from rest_framework.views import *


class ShipperView(ListCreateAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer


class OurServiceView(ListCreateAPIView):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer


class CareerView(ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class CareerUserView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            queryset = Career.objects.get(pk=pk)
            serializer = CareerUserSerializer(queryset)
        else:
            queryset = Career.objects.all()
            serializer = CareerUserSerializer(queryset, many=True)
        return Response(serializer.data)


class AboutUsView(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class CarrierView(ListCreateAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer


class ContactUserView(ListCreateAPIView):
    queryset = ContactUser.objects.all()
    serializer_class = ContactUserSerializer
