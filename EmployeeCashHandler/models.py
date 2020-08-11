from django.db import models
from users.models import Employee
from simple_history.models import HistoricalRecords



class CashDrawerCheckout(models.Model):
    start_bal = models.FloatField()
    end_bal = models.FloatField()
    datetime_in = models.DateTimeField()
    datetime_out = models.DateTimeField()
    employee = models.ForeignKey(Employee)
    history=HistoricalRecords()

class Store(models.Model):
    storename = models.CharField(max_length=50)

class Order(models.Model):
    order_id = models.IntegerField()
    holder = models.ForeignKey(Employee, blank=True, null=True) 
    
class LineItem(models.Model):
    sku = models.CharField(max_length = 100)
    product_name = models.CharField(max_length = 100)
    variant = models.CharField(max_length = 100, blank = True, null = True)
    rewardsused = models.BooleanField()
    pre_tax_price = models.FloatField()
    post_tax_price = models.FloatField()
