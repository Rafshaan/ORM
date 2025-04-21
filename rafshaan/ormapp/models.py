from django.db import models
from django.contrib import admin
class Movie (models.Model):
    user_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    mobile_no=models.IntegerField()
    email=models.EmailField()
    moviename=models.CharField(max_length=100)
    no_of_seats=models.IntegerField()
    date=models.DateField()
    
 
class MovieAdmin(admin.ModelAdmin):
    list_display=('user_id','name','moviename','no_of_seats','date')