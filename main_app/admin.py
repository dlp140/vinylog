from django.contrib import admin
from .models import Record, Collection, Photo

# Register your models here.
admin.site.register(Record)
admin.site.register(Collection)
admin.site.register(Photo)