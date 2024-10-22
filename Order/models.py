from django.db import models
from AdminCity.models import City
from django.contrib.auth.models import User


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=15,default=None)
    address = models.TextField()
    city_id = models.ForeignKey(City,to_field='city_id',on_delete=models.CASCADE,default=None)
    zipcode = models.CharField(max_length=10)
    order_datetime = models.DateTimeField(auto_now_add=True) 
    shipping_charge_order = models.DecimalField(max_digits=10, decimal_places=2,default=None)
    subtotal_order = models.DecimalField(max_digits=10, decimal_places=2,default=None)
    finaltotal_order = models.DecimalField(max_digits=10, decimal_places=2,default=None)



    class Meta:
        db_table = 'tbl_order'

    @property
    def row_number(self):
        queryset = Order.objects.order_by('order_id')
        row_number = list(queryset).index(self) + 1
        return row_number