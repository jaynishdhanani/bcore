from django.db import models
from AdminCategory.models import Category

class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category,to_field='category_id',on_delete=models.CASCADE,default=None)
    subcategory_name = models.CharField(max_length=100)
    subcategory_image = models.CharField(max_length=100, default='abc')
    subcategory_description = models.TextField()

    class Meta:
        db_table = 'tbl_subcategory'

    @property
    def row_number(self):
        queryset = SubCategory.objects.order_by('subcategory_id')
        row_number = list(queryset).index(self) + 1
        return row_number