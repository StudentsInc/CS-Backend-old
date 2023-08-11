from django.db import models
from account_app.models import ModelMixin, User
from ckeditor.fields import RichTextField


# Create your models here.

class Country(ModelMixin):
    country_name = models.CharField(max_length=50)
    country_code = models.IntegerField()

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['country_name', ]


class MajorSetup(ModelMixin):
    MAJOR_TYPE_CHOICE = (
        ('Bachelor', 'Bachelor'),
        ('Masters', 'Masters')
    )
    major_name = models.CharField(max_length=255, null=True, blank=True)
    major_description = models.TextField(null=True, blank=True)
    major_type = models.CharField(max_length=50, choices=MAJOR_TYPE_CHOICE, default='Bachelor')

    def __str__(self):
        return str(self.major_name)

    class Meta:
        ordering = ['-id', ]


class SchoolProfile(ModelMixin):
    objects = None
    school_name = models.CharField(max_length=255)
    banner_image = models.ImageField(upload_to='school-profile/banner-images/', blank=True, null=True)
    school_logo = models.ImageField(upload_to='school-profile/school-logo/', blank=True, null=True)
    location = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_no = models.CharField(max_length=17, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    world_rank = models.CharField(max_length=500, null=True, blank=True)
    country_rank = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name = 'School Profile'
        verbose_name_plural = 'School Profiles'
        ordering = ['-id', ]


class SchoolGallery(ModelMixin):
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE)
    images = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'School Gallery'
        verbose_name_plural = 'School Galleries'
        ordering = ['-id', ]


class SchoolMajor(ModelMixin):
    objects = None
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE)
    major = models.ForeignKey(MajorSetup, on_delete=models.CASCADE)
    credit_hours = models.CharField(max_length=20, null=True, blank=True)
    annual_tution_fee_local = models.IntegerField(null=True, blank=True)
    annual_tution_fee_international = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-id', ]


class SelectedSchool(ModelMixin):
    objects = None
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE)
