from django.db import models
from account_app.models import ModelMixin
from colorfield.fields import ColorField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Banner(ModelMixin):
    banner_image = models.ImageField(upload_to='career-studio/home/banner/', blank=True, null=True)
    banner_background_image = models.ImageField(upload_to='career-studio/home/banner/', blank=True, null=True)
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    heading_color = ColorField()
    content_color = ColorField()
    TEXT_STYLE_CHOICE = (
        ('LEFT', 'LEFT'),
        ('RIGHT', 'RIGHT'),
        ('CENTER', 'CENTER')
    )
    text_style = models.CharField(max_length=20, choices=TEXT_STYLE_CHOICE, default='"LEFT')
    button_text = models.CharField(max_length=100)
    button_url1 = models.CharField(max_length=300, null=True, blank=True)
    button_background = ColorField()
    button_text_color = ColorField()
    button_text2 = models.CharField(max_length=100, null=True, blank=True)
    button_url2 = models.CharField(max_length=300, null=True, blank=True)
    button_background2 = ColorField()
    button_text_color2 = ColorField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        ordering = ['-id', ]


#

class OurSkill(ModelMixin):
    skill_name = models.CharField(max_length=100)
    content = RichTextUploadingField()

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Our Skills'
        ordering = ['-id', ]


class About(ModelMixin):
    objects = None
    image = models.ImageField(upload_to='career-studio/home/about/', blank=True, null=True)
    background_image = models.ImageField(upload_to='career-studio/home/about/', blank=True, null=True)
    heading = models.CharField(max_length=200)
    content = RichTextField()
    button_text = models.CharField(max_length=100, null=True, blank=True)
    button_url = models.CharField(max_length=300, null=True, blank=True)
    button_background = ColorField()
    button_color = ColorField()
    long_content = RichTextField( null=True, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
        ordering = ['-id', ]


class HowItWorks(ModelMixin):
    heading = models.CharField(max_length=100)
    content = RichTextField()
    step = models.IntegerField()

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'How It Work'
        verbose_name_plural = 'How It Works'
        ordering = ['-id', ]


class Testimonials(ModelMixin):
    heading = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=55)
    image = models.ImageField(upload_to='career-studio/home/testimonials/', blank=True, null=True)
    content = RichTextField()

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['-id', ]


class Brand(ModelMixin):
    objects = None
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='career-studio/home/brand/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'
        ordering = ['-id', ]


class ContactUs(ModelMixin):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    DEPARTMENT_CHOICE = (
        ('DEPT1', 'DEPT1'),
        ('DEPT2', 'DEPT2')
    )
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICE, default='DEPT1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact Us'
        ordering = ['-id', ]


class Newsletter(ModelMixin):
    email = models.EmailField()

    def __str__(self):
        return self.email

    verbose_name = 'Newsletter'
    verbose_name_plural = 'Newsletters'
    ordering = ['-id', ]


class NewsletterText(ModelMixin):
    heading = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
