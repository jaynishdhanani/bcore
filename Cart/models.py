from django.db import models
from AdminProduct.models import Product
from AdminProduct.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product,to_field='product_id',on_delete=models.CASCADE,default=None)
    cart_qty = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = 'tbl_cart'

    @property
    def total_price(self):
        total = float(self.cart_qty) * float(self.product_id.product_price)
        return total