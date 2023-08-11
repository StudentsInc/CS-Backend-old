from django.db import models
from account_app.models import ModelMixin
from ckeditor.fields import RichTextField

# Create your models here.
ALIGN_CHOICE = (
    ('left', 'LEFT'),
    ('right', 'RIGHT'),
)


class Educator(ModelMixin):
    objects = None
    heading = models.CharField(blank=True, null=True, max_length=255, default='')
    subheading = RichTextField(blank=True, null=True, default='')
    EDUCATOR_TYPE_CHOICE = (
        ('high-school', 'High School'),
        ('post-secondary', 'Post Secondary'),
    )
    educator_type = models.CharField(max_length=255, choices=EDUCATOR_TYPE_CHOICE, default='"high-school')

    def __str__(self):
        if self.heading:
            return str(self.heading)
        return self.id

    class Meta:
        verbose_name = 'Educators'
        verbose_name_plural = 'Educators'
        ordering = ['-id', ]


class HighSchoolTabItems(ModelMixin):
    image = models.ImageField(upload_to='career-studio/educators/high-school', blank=True, null=True)
    heading = models.CharField(default='Surveys', max_length=255)
    subheading = models.CharField(default='Assessments that Build Self-Knowledge', max_length=255)
    align = models.CharField(max_length=10, choices=ALIGN_CHOICE, default='left')
    body = models.TextField(default='Students complete interactive personality, interests and learning '
                                    'style assessments to help them better understand their unique strengths and interests.')

    def __str__(self):
        if self.heading:
            return str(self.heading)
        return self.id

    class Meta:
        verbose_name = 'High School Tab Item(s)'
        verbose_name_plural = 'High School Tab Item(s)'
        ordering = ['-id', ]


class CollegeLifeItems(ModelMixin):
    image = models.ImageField(upload_to='career-studio/educators/college-life', blank=True, null=True)
    heading = models.CharField(default='School Administrators', max_length=255)
    body = models.TextField(
        default='')

    learn_more = models.CharField(default='', max_length=255, blank=True, null=True)

    def __str__(self):
        if self.heading:
            return str(self.heading)
        return self.id

    class Meta:
        verbose_name = 'College Life Tab Item(s)'
        verbose_name_plural = 'College Life Tab Item(s)'
        ordering = ['-id', ]


class HighSchool(ModelMixin):
    objects = None
    heading = models.CharField(blank=True, null=True, max_length=255,
                               default='Prepare Students for a Successful Future')
    subheading = RichTextField(blank=True, null=True, default='')
    high_school_tab_items = models.ManyToManyField(HighSchoolTabItems, related_name='high_school_tab', blank=True)

    college_heading = models.CharField(blank=True, null=True, max_length=255,
                                       default='Create a College, Career and Life Readiness Culture')
    college_subheading = models.TextField(blank=True, null=True, default='')
    college_life_items = models.ManyToManyField(CollegeLifeItems, related_name='college_life', blank=True)

    def __str__(self):
        if self.heading:
            return str(self.heading)
        return self.id

    class Meta:
        verbose_name = 'High School'
        verbose_name_plural = 'High School'
        ordering = ['-id', ]


class PostSecondaryTabImages(models.Model):
    file = models.FileField(null=True, blank=True)
    align = models.CharField(max_length=10, choices=ALIGN_CHOICE, default='left')


class PostSecondaryTabItems(ModelMixin):
    image = models.ManyToManyField(PostSecondaryTabImages, blank=True)
    heading = models.CharField(default='Surveys', max_length=255)
    subheading = models.CharField(default='Assessments that Build Self-Knowledge', max_length=255)
    align = models.CharField(max_length=10, choices=ALIGN_CHOICE, default='left')
    body = models.TextField(default='Body Text')

    def __str__(self):
        if self.heading:
            return self.heading
        return str(self.id)


class PostSecondary(ModelMixin):
    objects = None
    heading = models.CharField(blank=True, null=True, max_length=255,
                               default='Unite your Campus Around Student Success')
    secondary_tab_items = models.ManyToManyField(PostSecondaryTabItems, related_name='secondary_tab', blank=True)

    def __str__(self):
        if self.heading:
            return self.heading
        return str(self.id)
