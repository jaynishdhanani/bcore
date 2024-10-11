from django.db import models
from AdminProduct.models import Product
from Order.models import Order
# Create your models here.
class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product,to_field='product_id',on_delete=models.CASCADE,default=None)
    order_id = models.ForeignKey(Order,to_field='order_id',on_delete=models.CASCADE,default=None)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'tbl_items'

    @property
    def total_price(self):
        total = float(self.qty) * float(self.product_id.product_price)
        return total