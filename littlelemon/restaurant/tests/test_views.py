from django.test import TestCase, Client
from restaurant.models import *
from restaurant.serializers import MenuSerializer,BookingSerializer
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json
from rest_framework import status
from django.utils import timezone


class MenuItemViewTest(TestCase):
     
    def setUp(self) -> None:
        menu1 = Menu.objects.create(title="Icecream",price=5.75,inventory=5)
        menu2 = Menu.objects.create(title="Mocha",price=4.50,inventory=7)
        menu3 = Menu.objects.create(title="Lemonade",price=1.50,inventory=100)
        self.client = Client()
    
    def test_getall(self):
        response = self.client.get(reverse('menu_api'))
        
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)

class BookingTesTCase(APITestCase):

    def setUp(self):
        self.client=APIClient()
        self.user = User.objects.create_user(username='testuser',password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.booking1 = Booking.objects.create(name='shanaya',No_of_guests=2,BookingDate=timezone.now())
        self.booking2 = Booking.objects.create(name='Twain',No_of_guests=3,BookingDate=timezone.now())
        self.valid_data={
            'name':'Mark',
            'No_of_guests':2,
            'BookingDate':timezone.now()
        }
        self.invalid_data= {
            'name':'',
            'No_of_guests':'',
            'BookingDate':''
        }

    def test_getallBooking(self):
        
        response=self.client.get(reverse('bookingapi-list'))
        bookings=Booking.objects.all()
        serializer=BookingSerializer(bookings,many=True)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
         
    def test_createbookingvalid(self):
        
        response=self.client.post(reverse('bookingapi-list'),data=json.dumps(self.valid_data, cls=DjangoJSONEncoder),content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_createbookinginvalid(self):
        
        response=self.client.post(reverse('bookingapi-list'),data=json.dumps(self.invalid_data,cls=DjangoJSONEncoder),content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_getsinglebooking(self):
        
        response=self.client.get(reverse('bookingapi-detail',kwargs={'pk':self.booking1.pk}))
        booking=Booking.objects.get(pk=self.booking1.pk)
        serializer=BookingSerializer(booking)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)