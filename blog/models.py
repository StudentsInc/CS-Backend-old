from django.db import models
from account_app.models import ModelMixin
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from career_studio.utils import unique_slug_generator


def get_thumbnail_uploading_path(instance, filename):
    today = datetime.datetime.now()
    return f'blogs/{today.strftime("%Y")}/{today.strftime("%m")}/{today.strftime("%d")}/{instance.slug}/thumbnail.png'


def get_cover_image_uploading_path(instance, filename):
    today = datetime.datetime.now()
    return f'blogs/{today.strftime("%Y")}/{today.strftime("%m")}/{today.strftime("%d")}/{instance.slug}/coverimage.png'


class Blog(ModelMixin):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    introduction = models.TextField(verbose_name='Short description')
    description = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to=get_thumbnail_uploading_path, verbose_name='Blog thumbnail')
    cover_image = models.ImageField(upload_to=get_cover_image_uploading_path, verbose_name='Blog CoverImage')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-id', ]


@receiver(pre_save, sender=Blog)
def blog_slug_generator(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
