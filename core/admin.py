from django.contrib import admin
from core import models

admin.site.register(models.News)
admin.site.register(models.Category)