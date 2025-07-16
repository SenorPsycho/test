from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    class products(models.Model):
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        model = models.DecimalField(max_length=100)        
        description = models.TextField(null=True, blank=True)
        stock = models.PositiveIntegerField(default=0)        


class Student:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. I am {self.height} cm tall and weigh {self.weight} kg."
    
class Animal(self):
    def speak(self):
        print("Animal function called")
        

class Dog(Animal):
    super().speak()
    def speak(self):
        super().speak()
        print("Dog function called")
    def parent_speak(self):
        super().speak()
    
animal = Animal()
animal.speak()

dog = Dog()
dog.speak()