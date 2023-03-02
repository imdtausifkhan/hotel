from .models import (Hotel, Customer, Room, Food)
from rest_framework import serializers
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_location', 'hotel_website']

    def validate_hotel_name(self, attrs):
        hotel_name = Hotel.objects.filter(hotel_name=attrs)
        if hotel_name.exists():
            raise serializers.ValidationError("This Company already exist")
        return attrs

    def create(self, validated_data):
        hotel_d = Hotel.objects.create(
            hotel_name=validated_data['hotel_name'],
           # company_id=validated_data['company_id'],
            hotel_location=validated_data['hotel_location'],
            hotel_website=validated_data['hotel_website'],
        )
        hotel_d.save()
        data = hotel_d
        return data

    def update(self, instance, validated_data):
        if not instance.is_deleted:
            instance.hotel_name = validated_data['hotel_name']
            instance.hotel_location = validated_data['hotel_location']
            instance.hotel_website = validated_data['hotel_website']
            instance.hotel_website = validated_data['hotel_id']
            instance.save()
        else:
            raise serializers.ValidationError({"detail": "User does not exists"})
        return instance
    
    def get_hotel(cls,cust:Customer):
        comp = Hotel.objects.filter(id=cust.hotel.id).values()
        return hotel
    

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("name","phone","email","password")
    
    def create(self, validated_data):
        obj = Customer.objects.create(
            name=validated_data['name'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            password=validated_data['password'],

        )
        return obj

    # def get_company(cls,cust:Customer):
    #     comp = Company.objects.filter(id=cust.company.id).values()
    #     return comp
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("name","price", "image")
    
    def create(self, validated_data):
        obj = Room.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
            #category=validated_data['category'],
            image=validated_data['image'],

        )
        return obj

    def get_room(cls,cust:Customer):
        pro = Room.objects.filter(id=cust.room.id).values()
        return room
        

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("name","phone","id")
    
    def create(self, validated_data):
        obj = Supplier.objects.create(
            name=validated_data['name'],
            phone=validated_data['phone'],
            # id=validated_data['id'],
        )
        return obj

    def get_food(cls,cust:Customer):
        supp = Food.objects.filter(id=cust.food.id).values()
        return food