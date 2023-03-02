from django.urls import path
# from adminportal.views imp
from .views import (HotelView, HotelView, CustomerView, RoomView, FoodView)
                    
urlpatterns = ([        
        path('hotel/', HotelView.as_view(), name = 'hotel'),
        path('customer/', CustomerView.as_view(), name='customer'),
        path('room/', RoomView.as_view(), name='room'),
        path('food/', FoodView.as_view(), name='food'),
        
])