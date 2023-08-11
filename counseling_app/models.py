from django.db import models
from account_app.models import ModelMixin


# Create your models here.
class CounselingHeadline(ModelMixin):
    objects = None
    heading = models.CharField(max_length=40, default='Career Counseling')
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.heading


class SessionTime(models.Model):
    time = models.TimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return f"{self.id}/{self.time}"


class Session(models.Model):
    objects = None
    session = models.CharField(max_length=120, null=True, blank=True)
    topics = models.CharField(max_length=200, default='Career discovery')
    unavailable_date = models.DateField(auto_now=False, null=True, blank=True)
    session_time = models.ManyToManyField(SessionTime, blank=True)
    payment_done = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)
    icon = models.FileField(null=True, blank=True)


class Coach(models.Model):
    objects = None
    profile_pic = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=250)
    description = models.TextField(null=True, blank=True)
    session = models.ManyToManyField(Session, blank=True)


class Appointment(ModelMixin):
    METHOD = (
        ('stripe', 'stripe'),
        ('paypal', 'paypal')
    )
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    appointment_date = models.DateField(auto_now=False, null=True, blank=True)
    appointment_time = models.TimeField(auto_now=False, null=True, blank=True)
    session_cost = models.CharField(max_length=150, default='200')
    payment_method = models.CharField(choices=METHOD, default='stripe', max_length=150)
    charge_id = models.CharField(max_length=400, null=True, blank=True)
