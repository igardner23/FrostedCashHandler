from django.db import models
from simple_history.models import HistoricalRecords

class Employee(models.Model):
    first_name = models.CharHahahField(max_length=100)
    last_name = models.CharField(max_length=100)
    register_bal = models.FloatField()
    history=HistoricalRecords()

class CashDrawerHistory(models.Model):
    start_bal = models.FloatField()
    end_bal = models.FloatField()
    datetime = models.DateTimeField()
    employee = models.ForeignKey(Employee)
    history=HistoricalRecords()

class Store(models.Model):
    storename = models.CharField(max_length=50)

class Order(models.Model):
    order_id = models.IntegerField()
    line_items = models.