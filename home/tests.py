from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Item
#Tests done by JohnW

class ListingTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", first_name="tester", email="test@email.com", password="secret"
        )

        cls.item =Item.objects.create(
            title="A cool title",
            description="A detailed description",
            price=100.00,
            condition="Bad",
            user=cls.user
        )
        
    def test_item_model(self):
        self.assertEqual(self.item.title, "A cool title")
        self.assertEqual(self.item.description, "A detailed description")
        self.assertEqual(self.item.price, 100.00)
        self.assertEqual(self.item.condition, "Bad")
        self.assertEqual(self.item.user.username, "testuser")
        self.assertEqual(str(self.item), "A cool title - tester")
        #self.assertEqual(self.item.get_absolute_url(), "/items/1/")
        
    
    def test_url_exits_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    
    def test_url_exits_at_correct_location_detailview(self):
        response = self.client.get("/items/1/")
        self.assertEqual(response.status_code, 200)