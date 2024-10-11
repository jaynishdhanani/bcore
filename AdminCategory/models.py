from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_image = models.CharField(max_length=100, default='abc')

    class Meta:
        db_table = 'tbl_category'

    @property
    def row_number(self):
        queryset = Category.objects.order_by('category_id')
        row_number = list(queryset).index(self) + 1
        return row_number