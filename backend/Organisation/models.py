from django.db import models
from simple_history.models import HistoricalRecords



class Employee(models.Model):
    first_name = models.CharField(max_length=50) 
    surname = models.CharField(max_length=50) 
    age = models.PositiveIntegerField() 
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=15) 
    address = models.CharField(max_length=200) 
    department = models.CharField(max_length=100) 
    role = models.CharField(max_length=100) 
    employer = models.ForeignKey(Employer,on_delete=models.CASCADE) 
    manager = models.ForeignKey('Manager',on_delete=models.SET_NULL,null=True,related_name='managed_employees') 
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.first_name} {self.surname}"

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Individual(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE) 
    history = HistoricalRecords() 

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Individual'
        verbose_name_plural = 'Individuals'


class Organization(models.Model):
    name = models.CharField(max_length=100) 
    address = models.CharField(max_length=200) 
    history = HistoricalRecords() 


class Manager(models.Model):
    first_name = models.CharField(max_length=50) 
    surname = models.CharField(max_length=50) 
    age = models.PositiveIntegerField() 
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=15) 
    address = models.CharField(max_length=200) 
    department = models.CharField(max_length=100) 
    role = models.CharField(max_length=100) 
    employer = models.ForeignKey(Employer,on_delete=models.CASCADE) 
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.first_name} {self.surname}"

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'


class Employer(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=100) 
    company_name = models.CharField(max_length=100) 
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE) 
    history = HistoricalRecords() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self): 
        return self.name

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

