from django.db import models
from account_app.models import ModelMixin, User
from ckeditor.fields import RichTextField


class Skill(ModelMixin):
    SKILL_TYPE_CHOICE = (
        ('soft', 'Soft'),
        ('hard', 'Hard')
    )
    skill_type = models.CharField(max_length=5, choices=SKILL_TYPE_CHOICE, default='hard')
    skill_name = models.CharField(max_length=65)

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['-id', ]


class AlternativeTitles(ModelMixin):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Alternative Title'
        verbose_name_plural = 'Alternative Titles'
        ordering = ['-id', ]


class Country(ModelMixin):
    country_name = models.CharField(max_length=50)
    country_code = models.IntegerField()

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['country_name', ]


class CareerProfile(ModelMixin):
    PROFILE_TYPE_CHOICE = (
        ('Artistic', 'Artistic'),
        ('Social', 'Social'),
        ('Enterprising', 'Enterprising'),
        ('Investigative', 'Investigative'),
        ('Conventional', 'Conventional'),
        ('Realistic', 'Realistic')
    )
    profile_type = models.CharField(max_length=25, choices=PROFILE_TYPE_CHOICE, default='Artistic')
    name = models.CharField(max_length=100)
    BANNER_TYPE_CHOICE = (
        ('Video', 'Video'),
        ('Image', 'Image')
    )
    banner_type = models.CharField(max_length=10, choices=BANNER_TYPE_CHOICE, default='Video')
    banner_url = models.CharField(max_length=255)
    alternative_title = models.ManyToManyField(AlternativeTitles)
    soft_skill = models.ManyToManyField(Skill, related_name='soft_skill')
    hard_skill = models.ManyToManyField(Skill, related_name='hard_skill')
    profile_description = RichTextField()
    profile_image = models.ImageField(upload_to='career-profile/images/', blank=True, null=True)
    career_detail = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Career Profile'
        verbose_name_plural = 'Career Profiles'
        ordering = ['-id', ]


class CareerProfileGlance(ModelMixin):
    career_profile = models.ForeignKey(CareerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    RATING_CHOICE = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )
    rating = models.CharField(max_length=15, choices=RATING_CHOICE, default='Low')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Career Profile Glance'
        verbose_name_plural = 'Career Profile Glance'
        ordering = ['-id', ]


class AverageSalary(ModelMixin):
    career_profile = models.ForeignKey(CareerProfile, on_delete=models.CASCADE)
    location = models.ForeignKey(Country, on_delete=models.CASCADE)
    avg_sal_entry = models.CharField(max_length=50)
    avg_sal_mid = models.CharField(max_length=50)
    avg_sal_senior = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Average Salary'
        verbose_name_plural = 'Average Salaries'
        ordering = ['-id', ]


class CareerEducationRequirement(ModelMixin):
    career_profile = models.ForeignKey(CareerProfile, on_delete=models.CASCADE)
    description = RichTextField()
    bachelor_degree = models.BooleanField(default=False)
    master_degree = models.BooleanField(default=False)
    college = models.CharField(max_length=255)
    specialisation = models.CharField(max_length=255)

    def __str__(self):
        return str(self.career_profile)

    class Meta:
        verbose_name = 'Career Education Requirement'
        verbose_name_plural = 'Career Education Requirements'
        ordering = ['-id', ]


class CareerCommonIndustries(ModelMixin):
    career_profile = models.ForeignKey(CareerProfile, on_delete=models.CASCADE)
    description = RichTextField()
    private = models.BooleanField(default=False)
    government = models.BooleanField(default=False)

    def __str__(self):
        return str(self.career_profile)

    class Meta:
        verbose_name = 'Career Common Industry'
        verbose_name_plural = 'Career Common Industries'
        ordering = ['-id', ]


class CareerCommonIndustriesBreakup(ModelMixin):
    common_career = models.ForeignKey(CareerCommonIndustries, models.CASCADE)
    TYPE_CHOICE = (
        ('Private', 'Private'),
        ('Government', 'Government')
    )
    type = models.CharField(choices=TYPE_CHOICE, default='Private', max_length=12)
    title = models.CharField(max_length=255)
    percentage = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Career Common Industries Breakup'
        verbose_name_plural = 'Career Common Industries Breakup'
        ordering = ['-id', ]


class AssessmentCategory(ModelMixin):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Assessment Category'
        verbose_name_plural = 'Assessment Categories'
        ordering = ['-id', ]


class Type(ModelMixin):
    assessment_Category = models.ForeignKey(AssessmentCategory, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['-id', ]


class Assessment(ModelMixin):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    question = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Assessment'
        verbose_name_plural = 'Assessments'
        ordering = ['-id', ]


class UserAssessment(ModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    ANSWER_TYPE_CHOICE = (
        ('Strongly Agree', 'Strongly Agree'),
        ('Agree', 'Agree'),
        ('Neutral', 'Neutral'),
        ('Disagree', 'Disagree'),
        ('Strongly Disagree', 'Strongly Disagree')
    )
    answer_type = models.CharField(max_length=100, choices=ANSWER_TYPE_CHOICE, default='Agree')
    answer = RichTextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'User Assessment'
        verbose_name_plural = 'User Assessments'
        ordering = ['-id', ]


class MajorSetup(ModelMixin):
    major_name = models.CharField(max_length=255)
    major_description = models.TextField()
    MAJOR_TYPE_CHOICE = (
        ('Bachelor', 'Bachelor'),
        ('Masters', 'Masters')
    )
    major_type = models.CharField(max_length=50, choices=MAJOR_TYPE_CHOICE, default='Bachelor')

    def __str__(self):
        return self.major_name

    class Meta:
        ordering = ['-id', ]


class SchoolProfile(ModelMixin):
    objects = None
    school_name = models.CharField(max_length=255)
    banner_image = models.ImageField(upload_to='school-profile/banner-images/', blank=True, null=True)
    school_logo = models.ImageField(upload_to='school-profile/school-logo/', blank=True, null=True)
    location = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    email = models.EmailField()
    contact_no = models.CharField(max_length=17)
    website = models.CharField(max_length=255)
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
    images = models.URLField()

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
    credit_hours = models.CharField(max_length=20)
    annual_tution_fee_local = models.IntegerField()
    annual_tution_fee_international = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-id', ]


class SchoolMajorSubject(ModelMixin):
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE)
    school_major = models.ForeignKey(SchoolMajor, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    sub_desc = models.TextField()
    video_url = models.URLField()

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = 'Major Subject'
        verbose_name_plural = 'School Major Subjects'
        ordering = ['-id', ]


class SelectedSchool(ModelMixin):
    objects = None
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE)
