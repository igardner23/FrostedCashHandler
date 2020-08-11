from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    register_bal = models.FloatField()
    id = models.Like 

class CashDrawerHistory(models.Model):
    start_bal = models.FloatField()
    end_bal = models.FloatField()
    datetime = models.DateTimeField()
    employee = models.ForeignKey(Employee)

class Store(models.Model):
    storename = models.CharField(max_length=50)

class Order(models.Model):
    order_id = models.IntegerField()
    line_items = models.