from django.test import TestCase
from models import Menu

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
        
class MenuViewTest(TestCase):
    def setUp(self):
        item = Menu.objects.create(title="IceCream", price=90, inventory=100)
        self.assertEqual(item, "IceCream : 90")