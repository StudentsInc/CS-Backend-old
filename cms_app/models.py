from django.db import models
from account_app.models import ModelMixin
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from personality_test.models import QUESTION_TYPE, Job_Category, JobMaster

Career_Options = (
    ('artistic', 'artistic'),
    ('social', 'social'),
    ('enterprising', 'enterprising'),
    ('investigative', 'investigative'),
    ('conventional', 'conventional'),
    ('realistic', 'realistic'),
)

Work_Value_Category = (
    ('achievement', 'achievement'),
    ('independence', 'independence'),
    ('recognition', 'recognition'),
    ('relationships', 'relationships'),
    ('support', 'support'),
    ('working conditions', 'working conditions'),
)


class PrivacyPolicy(ModelMixin):
    page_title = models.CharField(max_length=50)
    body = RichTextUploadingField()

    def __str__(self):
        return self.page_title

    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policies'
        ordering = ['id', ]


class TermsAndCondition(ModelMixin):
    page_title = models.CharField(max_length=50)
    body = RichTextUploadingField()

    def __str__(self):
        return self.page_title

    class Meta:
        verbose_name = 'Term and Condition'
        verbose_name_plural = 'Terms and Conditions'
        ordering = ['id', ]


class AboutUs(ModelMixin):
    page_title = models.CharField(max_length=50)
    body = RichTextUploadingField()

    def __str__(self):
        return self.page_title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About Us'
        ordering = ['id', ]


class FAQ(ModelMixin):
    question = models.CharField(max_length=255)
    answer = RichTextUploadingField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['id', ]


class CareerLibrary(models.Model):
    career_options = models.CharField(max_length=100, choices=Career_Options, null=True, blank=True)
    category = models.CharField(max_length=100, choices=QUESTION_TYPE, null=True, blank=True)
    job_type = models.CharField(max_length=100, choices=Job_Category, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    picture = models.FileField(upload_to='career_library', null=True, blank=True)
    salary = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    graph = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.career_options


class CareerLibraryUser(ModelMixin):
    objects = None
    career_library = models.ForeignKey(JobMaster, on_delete=models.CASCADE, null=True, blank=True)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return self.created_by.email


class SelectCareer(ModelMixin):
    objects = None
    name = models.CharField(max_length=256, null=True, blank=True)
    education = models.CharField(max_length=256, null=True, blank=True)
    salary = models.CharField(max_length=256, null=True, blank=True)
    environment = models.CharField(max_length=256, null=True, blank=True)
    values = models.CharField(max_length=256, null=True, blank=True)
    votes = models.PositiveIntegerField(max_length=256, null=True, blank=True, default=0)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=256, null=True, blank=True)
    link = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(upload_to='career_image', null=True, blank=True)

    def __str__(self):
        return self.name


class CareerVotes(models.Model):
    career = models.ForeignKey(SelectCareer, on_delete=models.CASCADE, null=True, blank=True)
    guest_token = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.career


class RecommendationNot(ModelMixin):
    title = models.CharField(max_length=512, null=True, blank=True)
    is_recommendate = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CareerLibraryDetail(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    alternative_title = models.CharField(max_length=256, null=True, blank=True)
    low_salary = models.CharField(max_length=128, null=True, blank=True)
    mid_salary = models.CharField(max_length=128, null=True, blank=True)
    high_salary = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tasks = models.TextField(null=True, blank=True)
    soft_skill = models.TextField(null=True, blank=True)
    hard_skill = models.TextField(null=True, blank=True)
    responsibility = models.CharField(max_length=256, null=True, blank=True)
    hazard = models.CharField(max_length=256, null=True, blank=True)
    physical_activity = models.CharField(max_length=128, null=True, blank=True)
    decision_making = models.CharField(max_length=128, null=True, blank=True)
    repetitive = models.CharField(max_length=128, null=True, blank=True)
    competitive = models.CharField(max_length=128, null=True, blank=True)
    time_pressure = models.CharField(max_length=128, null=True, blank=True)
    job_zone = models.CharField(max_length=128, null=True, blank=True)
    majors = models.CharField(max_length=256, null=True, blank=True)
    education_data = models.CharField(max_length=256, null=True, blank=True)
    typical_industries = models.CharField(max_length=256, null=True, blank=True)
    video = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class SoftSkills(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    icon = models.ImageField(upload_to='career_profile/soft_skill', null=True, blank=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name


class HardSkills(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    icon = models.ImageField(upload_to='career_profile/soft_skill', null=True, blank=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name


class WorkValuesScores(models.Model):
    category = models.CharField(max_length=128, choices=Work_Value_Category, null=True, blank=True)
    value = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.category


class WorkValueItems(models.Model):
    objects = None
    category = models.CharField(max_length=128, choices=Work_Value_Category, null=True, blank=True)
    items = models.TextField(null=True, blank=True)
    category_type = models.CharField(max_length=128, null=True, blank=True)
    item_no = models.CharField(max_length=5, default='', null=True, blank=True)
    item_score = models.IntegerField(null=True, blank=True)
    multiply_no = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.items


class UserWorkValues(ModelMixin):
    objects = None
    category = models.ForeignKey(WorkValueItems, on_delete=models.SET_NULL, null=True, blank=True)
    score = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.category.category


class CareerValues(ModelMixin):
    ROW = (
        ('first', 'first'),
        ('second', 'second'),
        ('third', 'third')
    )

    objects = None
    title = models.CharField(max_length=400, default='')
    element_name = models.TextField(null=True, blank=True)
    data_value = models.IntegerField(null=True, blank=True)
    row = models.CharField(max_length=100, default='first', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.element_name == 'First Work Value High-Point':
            self.row = 'first'

        elif self.element_name == 'Second Work Value High-Point':
            self.row = 'second'

        elif self.element_name == 'Third Work Value High-Point':
            self.row = 'third'

        return super().save(*args, **kwargs)


class Major(ModelMixin):
    objects = None
    name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    typical_subjects = models.TextField(null=True, blank=True)
    typical_careers = models.TextField(null=True, blank=True)
    sample_lectures = models.TextField(null=True, blank=True)
    in_demand = models.TextField(max_length=20, null=True, blank=True)


class UserSelectedMajor(ModelMixin):
    objects = None
    major = models.ForeignKey(Major, on_delete=models.CASCADE)


class UserSelectedCareer(ModelMixin):
    objects = None
    career = models.ForeignKey(SelectCareer, on_delete=models.CASCADE)
    values = models.CharField(max_length=100, null=True, blank=True)


class MajorSubject(models.Model):
    objects = None
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    subject_name = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    video = models.TextField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     print(self.major, type(self.major))
        # return super(MajorSubject, self).save(*args, **kwargs)
