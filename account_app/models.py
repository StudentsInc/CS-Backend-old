from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from account_app.moder_manager import LanguageManager
from django.db.models import signals
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib import messages

# Create your models here.
STATUS_TYPE = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('blocked', 'Blocked')
)

LANG_TYPE = (
    ('English', 'en'),
    ('Arabic', 'ar')
)

USER_ROLE = (
    ('counsellor', 'counsellor'),
    ('student', 'student'),
)

Category_Type = (
    ('free', 'free'),
    ('paid', 'paid')
)

DATE_INPUT_FORMATS = ['%Y-%m-%d']


class ModelMixin(models.Model):
    """
        This mixins provide the default field in the models project wise
    """
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created",
                                   on_delete=models.CASCADE, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_updated",
                                   on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, default='active', choices=STATUS_TYPE, help_text=_('Status'))
    language_code = models.CharField(max_length=35, default='English', choices=LANG_TYPE)
    # lang_objects = LanguageManager()

    class Meta:
        abstract = True
        # default_manager_name = 'lang_objects'


class Profile(ModelMixin):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    picture = models.FileField(upload_to='user/profile', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=25, choices=GENDER, default='Male')
    user_role = models.CharField(max_length=100, choices=USER_ROLE, default='student')

    def save(self, *args, **kwargs):
        if self.id is not None:
            return super(Profile, self).save()
        query = Profile.objects.filter(created_by=self.created_by)
        if len(query) <= 1:
            return super(Profile, self).save()
        raise ValueError("User already have Profile.")


class Otp(ModelMixin):
    OTP_VERIFY = (
        ('true', 'True'),
        ('false', 'False'),
    )
    OTP_TYPE = (
        ('register', 'register'),
        ('forgot', 'forgot'),
    )

    otp = models.IntegerField(default=0)
    type = models.CharField(max_length=20, choices=OTP_TYPE, default='forgot', null=True, blank=True)
    verify = models.CharField(choices=OTP_VERIFY, default='false', max_length=100)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    messages = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.user.email


def notification_create(user, message):
    # get user instanse
    user = User.objects.get(pk=user.pk)

    # create notification
    notification = Notification(user=user, messages=message)
    notification.save()
    return True


class CounsellorAppointment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='student')
    counsellor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='counsellor')
    session = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=100, choices=Category_Type)
    date_created = models.DateTimeField(auto_now_add=True)


class GuestUser(models.Model):
    token = models.CharField(max_length=256, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
