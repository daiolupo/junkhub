from django.conf import settings
from django.db import models
from django.urls import reverse


#Model of the item listed for sale.
class Item(models.Model):
    # A tuple containing a selection of choices for the items condition
    CONDITION_CHOICES = [
        ("Brand new condition", "New"),
        ("Near new condition well looked after", "Good"),
        ("Average condition", "OK"),
        ("Poor condition old and well worn", "Bad"),
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    # Using djangos preffered currency data type
    price = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=100)
    # Each item listed will need to be assigned a user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title + ' - ' + self.user.first_name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})

#Model for comments that are added to items
class Comment(models.Model):
    # The related item the comment applies to.
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    #Using the current time when the comment is created.
    time = models.DateTimeField(auto_now_add=True)
    #the author of the comment
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    #the actual content of the comment - the only thing the user actually edits
    body = models.CharField(max_length=255)
    
    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("home")
  