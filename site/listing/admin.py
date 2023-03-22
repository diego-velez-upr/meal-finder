from django.contrib import admin
from .models import Food

# Adds the food DB table to the admin page, allowing admins to control them.
admin.site.register(Food)
