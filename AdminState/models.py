from django.db import models

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_state'

    @property
    def row_number(self):
        queryset = State.objects.order_by('state_id')
        row_number = list(queryset).index(self) + 1
        return row_number