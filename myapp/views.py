from django.shortcuts import render
from .helpers import http_response, status
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import (Hotel, Customer, Room,Food)
from .serializers import (HotelSerializer, CustomerSerializer, FoodSerializer, RoomSerializer)
# Create your views

class HotelView(generics.CreateAPIView, generics.UpdateAPIView, generics.ListAPIView, generics.DestroyAPIView):
    
    def get(self, request, *args, **kwargs):
        users = Hotel.objects.filter(is_deleted=False)
        serializer = HotelSerializer(users, many=True)
        return http_response(data=serializer.data, message='thank for your review', 
                            status_code=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        
        serializer = HotelSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(
                {
                    'error_message': 'Please correct the following errors.',
                    'errors': serializer.errors,
                }
            )
        serializer.save()
        return http_response(data=serializer.data, message='thank for your review', 
                            status_code=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        try:
            user = Hotel.objects.get(id=json.loads(request.body)['id'])
        except Hotel.DoesNotExist:
            raise serializers.ValidationError({"detail": "Company does not exists"})
        serializer = HotelSerializer(user, data=request.data)
        if not serializer.is_valid():
            raise ValidationError(
                {
                    'error_message': 'Please correct the following errors.',
                    'errors': serializer.errors,
                }
            )
        serializer.save()
        return http_response(data=serializer.data, message='thank for your review', 
                            status_code=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        hotel_id = request.data['id']
        if hotel_id is None:
            raise ValidationError(
                {
                    'error': 'company ID is required',
                    'status': False
                }
            )
        hotel = Hotel.objects.get(id=company_id)
        if not hotel.is_deleted:
            hotel.is_deleted = True
            hotel.save()
        else:
            raise serializers.ValidationError({"detail": "Company does not exists"})
        return http_response(data={}, message='thank for your review',
                             status_code=status.HTTP_200_OK)

class CustomerView(generics.CreateAPIView,generics.UpdateAPIView):

    def post(self,request, *args, **kwargs): 
        serializer = CustomerSerializer(data=request.data)
        if not serializer.is_valid():
                raise ValidationError(
                    {
                        'error_message': 'Please correct the following errors.',
                        'errors': serializer.errors,
                    }
                )
        serializer.save()
        return http_response(data=serializer.data,message='thank for your review',status_code=status.HTTP_200_OK)

class RoomView(generics.CreateAPIView,generics.UpdateAPIView):

    def post(self,request, *args, **kwargs): 
        serializer = RoomSerializer(data=request.data)
        if not serializer.is_valid():
                raise ValidationError(
                    {
                        'error_message': 'Please correct the following errors.',
                        'errors': serializer.errors,
                    }
                )
        serializer.save()
        return http_response(data=serializer.data,message='thank for your review',status_code=status.HTTP_200_OK)


class FoodView(generics.CreateAPIView,generics.UpdateAPIView):
    
    def post(self,request, *args, **kwargs): 
        serializer = FoodSerializer(data=request.data)
        if not serializer.is_valid():
                raise ValidationError(
                    {
                        'error_message': 'Please correct the following errors.',
                        'errors': serializer.errors,
                    }
                )
        serializer.save()
        return http_response(data=serializer.data,message='thank for your review',status_code=status.HTTP_200_OK)

