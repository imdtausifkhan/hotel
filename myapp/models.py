from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(('hotel_name'), max_length=50, null=True, blank=True)
   # company_id = models.CharField(('company_id'), max_length=50, null=True, blank=True)
    hotel_location = models.CharField(('hotel_location'), max_length=155, null=True, blank=True)
    hotel_website = models.CharField(('website'), null=True, blank=True, max_length=500)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True, db_index=True)
    is_deleted = models.BooleanField(default=True)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False


class Room(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
#    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.CharField(null=True , blank=True, max_length=50)

    @staticmethod
    def get_room_by_id(ids):
        return Room.objects.filter (id__in=ids)
    @staticmethod
    def get_all_room():
        return Room.objects.all()

    @staticmethod
    def get_all_room_by_categoryid(category_id):
        if category_id:
            return Room.objects.filter (category=category_id)
        else:
            return Room.get_all_products()

class Food(models.Model):
    name= models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    # id = models.CharField(max_length=20)

    @staticmethod
    def get_all_food():
        return Food.objects.all()

    def __str__(self):
        return (self.name, self.phone)

class Customer(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room =models.ForeignKey(Room, on_delete=models.CASCADE) 
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)

