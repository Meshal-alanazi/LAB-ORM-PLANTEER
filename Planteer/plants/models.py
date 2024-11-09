from django.db import models

# Create your models here.


class Plant(models.Model):
    class CategoryChoices(models.TextChoices):
        INDOOR = 'Tree', 'Tree'
        OUTDOOR = 'Fruit', 'Fruit'
        HERB = 'Herb', 'Herb'
        CACTUS = 'Cactus', 'Cactus'
    
    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/",default="images/default_FdKeTks.jpg")
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
