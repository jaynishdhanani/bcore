from django.db import models
from AdminSubCategory.models import SubCategory

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.CharField(max_length=100, default='abc')
    product_videourl = models.URLField(max_length=255, blank=True, null=True)
    product_description = models.TextField()
    product_specification = models.TextField()
    product_isactive = models.BooleanField(default=True)
    subcategory_id = models.ForeignKey(SubCategory,to_field='subcategory_id',on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = 'tbl_product'

    @property
    def cat_id(self):
        return self.subcategory_id.category_id.category_id

    @property
    def row_number(self):
        queryset = Product.objects.order_by('product_id')
        row_number = list(queryset).index(self) + 1
        return row_number
    
    @property
    def row_active(self):
        if self.product_isactive == True:
            return "Yes"
        else:
            return "No"