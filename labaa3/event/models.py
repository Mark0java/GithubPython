from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Event(models.Model):

    name = models.CharField(max_length=50)
    # time = models.DateField(auto_now=False)
    venue = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    event = models.ForeignKey(Event, verbose_name='event', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, verbose_name='owner', on_delete=models.CASCADE, null=True, blank=True, default=None)
    # owner = models.BooleanField(default=False)
    booked = models.ForeignKey(User, verbose_name='booked', on_delete=models.CASCADE,
                               null=True, blank=True, default=None, related_name='%(class)s_booked')
    seat = models.PositiveSmallIntegerField(primary_key=True)

    def __str__(self):
        return "%s - %s" % (self.seat, self.event)
