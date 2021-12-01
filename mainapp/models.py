from django.db import models
from account.models import User
import os
import random

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "mashroom/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Counties(BaseModel):
    county_name = models.CharField(max_length=255)

    def __str__(self):
        return self.county_name

class Mushroom(BaseModel):
    county_id =  models.ForeignKey(Counties,on_delete=models.CASCADE)
    mushroom_name = models.CharField(max_length=255)
    mushroom_image = models.ImageField(upload_to=upload_image_path)
    mushroom_description = models.TextField()

    def __str__(self):
        return self.mushroom_name

class MushroomPrediction(BaseModel):
    mushroom_date_price =  models.DateField()
    opening_price =  models.DecimalField(max_digits=20,decimal_places=2)
    closing_price =  models.DecimalField(max_digits=20,decimal_places=2)
    minimum_price =  models.DecimalField(max_digits=20,decimal_places=2)
    maximum_price =  models.DecimalField(max_digits=20,decimal_places=2)
    

    def __str__(self):
        return str(self.opening_price)


class MushroomCondition(BaseModel):
    mushroom_id = models.ForeignKey(Mushroom,on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)

    def __str__(self):
        return self.condition


class Sliderr(BaseModel):
    header1 =  models.CharField(max_length=255)
    body =  models.TextField()
    image =  models.ImageField(upload_to = upload_image_path)

    def __str__(self):
        return self.header1

class ImageOne(BaseModel):
    image =  models.ImageField(upload_to = upload_image_path)


class AboutUs(BaseModel):
    header1 =  models.CharField(max_length=255)
    body =  models.TextField()
    image =  models.ImageField(upload_to = upload_image_path)
    


    def __str__(self):
        return self.header1

class OurSerices(BaseModel):
    header1 =  models.CharField(max_length=255)
    body =  models.TextField()
    image =  models.ImageField(upload_to = upload_image_path)

    def __str__(self):
        return self.header1


class Backrgoundd(BaseModel):
    header1 =  models.CharField(max_length=255)
    body =  models.TextField()
    image = models.ImageField(upload_to = upload_image_path)

    def __str__(self):
        return self.header1




