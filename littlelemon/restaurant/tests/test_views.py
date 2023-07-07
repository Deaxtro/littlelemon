from django.test import TestCase, Client
from restaurant.models import *
from restaurant.serializers import MenuSerializer
from django.urls import reverse

class MenuItemViewTest(TestCase):
     
    def setUp(self) -> None:
        menu1 = Menu.objects.create(title="Icecream",price=5.75,inventory=5)
        menu2 = Menu.objects.create(title="Mocha",price=4.50,inventory=7)
        menu3 = Menu.objects.create(title="Lemonade",price=1.50,inventory=100)
        self.client = Client()
    
    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)