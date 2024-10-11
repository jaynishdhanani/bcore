from django.db import models
from AdminState.models import State


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    state_id = models.ForeignKey(State,to_field='state_id',on_delete=models.CASCADE,default=None)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2,default=None)

    class Meta:
        db_table = 'tbl_city'

    @property
    def row_number(self):
        queryset = City.objects.order_by('city_id')
        row_number = list(queryset).index(self) + 1
        return row_number