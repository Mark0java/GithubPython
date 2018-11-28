from django.contrib import admin
from . import models
from django.contrib.auth.models import User

admin.site.unregister(models.User)
admin.site.register(User)
admin.site.register(models.Event)
admin.site.register(models.Ticket)
