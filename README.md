# Ex02 Django ORM Web Application
## Date:10/04/2025 

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## ER DIAGRAM

![Screenshot 2025-05-10 131306](https://github.com/user-attachments/assets/70f9b1c0-df5b-493f-89ac-39f695f6162b)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
``` 
models.py
from django.db import models
from django.contrib import admin
class Employee(models.Model):
    User_name=models.CharField(max_length=100)
    email=models.EmailField()
    Phone_Number=models.IntegerField()
    MovieName=models.CharField(max_length=100)
    seats=models.IntegerField()
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('User_name','email','Phone_Number','MovieName','seats')

admin.py
from django.contrib import admin
from .models import Employee,EmployeeAdmin
admin.site.register(Employee,EmployeeAdmin)
```


## OUTPUT
![alt text](<Screenshot 2025-04-11 001511.png>)




## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
