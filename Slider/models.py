from django.db import models
from AdminSubCategory.models import SubCategory

class Slider(models.Model):
    slider_id = models.AutoField(primary_key=True)  # Auto-incremented ID
    slider_title = models.CharField(max_length=255)  # Title of the slider
    slider_subtitle = models.CharField(max_length=255, blank=True, null=True)  # Optional subtitle
    slider_button_text = models.CharField(max_length=100, blank=True, null=True)  # Optional button text
    slider_button_url = models.URLField(max_length=200, blank=True, null=True)  # Optional button URL
    slider_image = models.CharField(max_length=100, default='image')  # Image upload field

    class Meta:
        db_table = 'tbl_slider'

    @property
    def row_number(self):
        queryset = Slider.objects.order_by('slider_id')
        row_number = list(queryset).index(self) + 1
        return row_number