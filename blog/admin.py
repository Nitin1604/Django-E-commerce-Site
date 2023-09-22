# Folder Path : DjangoCourse\mac\blog\admin.py

from django.contrib import admin

# Register your models here.
from .models import Blogpost

admin.site.register(Blogpost)
