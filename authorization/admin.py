from django.contrib import admin

from authorization import models

# Register your models here.
admin.site.register(models.User)
