from django.test import TestCase
from restaurant.models import Menu

class TestMenu(TestCase):
    
    def setUp(self) -> None:
        self.menu1=Menu.objects.create(title="lollies",price=2.50,inventory=10)

    def test_create_item(self):
        item = Menu.objects.create(title='Icecream',price=5.75,inventory=20)
        self.assertEqual(str(item), 'Icecream: 5.75')
        self.assertEqual(item.inventory, 20)

    def test_get_item(self):
        menuitem=Menu.objects.get(id=self.menu1.id)
        self.assertEqual(str(menuitem), 'lollies: 2.50')
        self.assertEqual(menuitem.inventory, 10)