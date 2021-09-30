from rest_framework import serializers
from .models import *


class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = '__all__'


class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment',)


class CarrierSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(required=False, many=False)

    class Meta:
        model = Carrier
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'


class ContactUserSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(required=True,many=False)

    class Meta:
        model = ContactUser
        fields = '__all__'














