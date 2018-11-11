from django.db import models




class query(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    inquiry=models.TextField(null=True)    # null=True use -- table is created to enter new field

    def __str__(self):
        return self.name

CATEGORY_CHOICES = (
    ('Space planning and design','SPACE PLANNING AND DESIGN'),
    ('residential', 'RESIDENTIAL'),
    ('wardrobe and storage units','WARDROBE AND STORAGE UNITS'),
    ('astrology','ASTROLOGY'),
    ('modular kitchen','MODULAR KITCHEN'),
    ('bathroom','BATHROOM')
)

class appoint(models.Model):
    name=models.CharField(max_length=60 , null=True)
    email=models.EmailField(null = True)
    contact=models.IntegerField(null=True)
    address=models.CharField(max_length=150 , null=True)
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES,)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)

    def __str__(self):
        return self.name
