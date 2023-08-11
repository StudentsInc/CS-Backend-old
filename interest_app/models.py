from django.db import models
from account_app.models import ModelMixin, GuestUser
from django.db.models import Sum
from ckeditor.fields import RichTextField

# Create your models here.
from personality_test.constants import interest_constant

Question_Category = (
    ('artistic', 'artistic'),
    ('conventional', 'conventional'),
    ('social', 'social'),
    ('realistic', 'realistic'),
    ('investigative', 'investigative'),
    ('enterprising', 'enterprising'),
)

Report_Category = (
    ('creator', 'creator'),
    ('organizer', 'organizer'),
    ('helper', 'helper'),
    ('doer', 'doer'),
    ('thinker', 'thinker'),
    ('persuader', 'persuader'),
)


class InterestDetail(models.Model):
    heading = models.CharField(max_length=300, default="HOLLAND’S CODE ASSESSMENT")
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    assesment_button = models.CharField(max_length=300, default="HOLLAND’S CODE ASSESSMENT")
    duration = models.IntegerField(null=True, blank=True)
    total_question = models.IntegerField(help_text='Total No of Question', verbose_name='Total No of Question')
    objects = models.Manager()

    def __str__(self):
        return self.heading


class InterestQuestion(models.Model):
    interest_detail = models.ForeignKey(InterestDetail, on_delete=models.SET_NULL, null=True, blank=True)
    question_category = models.CharField(max_length=128, choices=Question_Category, default='')
    question_no = models.IntegerField(verbose_name='Question No')
    image = models.FileField(null=True, blank=True)
    question = models.TextField(default='')
    objects = models.Manager()

    class Meta:
        ordering = ['question_no', ]


class AnswerModel(ModelMixin):
    ANSWER_CHOICE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    question_detail = models.ForeignKey(InterestQuestion, on_delete=models.CASCADE)
    answer = models.CharField(help_text='like(1) to dislike(5)',
                              max_length=10)
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.answer)


class UserInterestTest(ModelMixin):
    EXAM_STATUS = (
        ('InProgress', 'InProgress'),
        ('Complete', 'Complete')
    )

    answer = models.ManyToManyField(AnswerModel, blank=True)
    start_time = models.DateTimeField(auto_now=False, null=True, blank=True)
    end_time = models.DateTimeField(auto_now=False, null=True, blank=True)
    time_left = models.CharField(max_length=100, null=True, blank=True)
    exam_status = models.CharField(max_length=30, choices=EXAM_STATUS, default='InProgress')
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager()

    def get_score(self):
        top_list = []
        artistic_score = self.answer.filter(question_detail__question_category='artistic').aggregate(Sum(
            'answer'))['answer__sum']
        conventional_score = self.answer.filter(question_detail__question_category='conventional').aggregate(Sum(
            'answer'))['answer__sum']
        social_score = self.answer.filter(question_detail__question_category='social').aggregate(Sum(
            'answer'))['answer__sum']
        realistic_score = self.answer.filter(question_detail__question_category='realistic').aggregate(Sum(
            'answer'))['answer__sum']
        investigative_score = self.answer.filter(question_detail__question_category='investigative').aggregate(Sum(
            'answer'))['answer__sum']
        enterprising_score = self.answer.filter(question_detail__question_category='enterprising').aggregate(Sum(
            'answer'))['answer__sum']
        score_dict = {
            'artistic': artistic_score,
            'conventional': conventional_score,
            'social': social_score,
            'realistic': realistic_score,
            'investigative': investigative_score,
            'enterprising': enterprising_score,
        }
        sorted_dict = dict(sorted(score_dict.items(), key=lambda item: item[1]))
        top_list.append(list(sorted_dict.keys())[-3::])
        print(top_list)
        new_list = []
        for i in top_list:
            for j in i:
                new_list.append(interest_constant[j])
        score_data = {
            'top_list': top_list, 'report_list': new_list, 'artistic_score': artistic_score,
            'conventional_score': conventional_score, 'social_score': social_score, 'realistic_score': realistic_score,
            'enterprising_score': enterprising_score, 'investigative_score': investigative_score}
        return score_data


class UserScores(ModelMixin):
    artistic_score = models.FloatField(default=0)
    conventional_score = models.FloatField(default=0)
    social_score = models.FloatField(default=0)
    realistic_score = models.FloatField(default=0)
    enterprising_score = models.FloatField(default=0)
    investigative_score = models.FloatField(default=0)
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.created_by:
            return self.created_by.email
        else:
            return "Guest User"

    def get_user_score(self):
        top_list = []
        score_dict = {
            'artistic': self.artistic_score,
            'conventional': self.conventional_score,
            'social': self.social_score,
            'realistic': self.realistic_score,
            'investigative': self.investigative_score,
            'enterprising': self.enterprising_score,
        }
        sorted_dict = dict(sorted(score_dict.items(), key=lambda item: item[1]))
        top_list.append(list(sorted_dict.keys())[-3::])
        new_list = []
        for i in top_list:
            for j in i:
                new_list.append(interest_constant[j])
        score_data = {
            'top_list': top_list, 'report_list': new_list, 'artistic_score': self.artistic_score,
            'conventional_score': self.conventional_score, 'social_score': self.social_score,
            'realistic_score': self.realistic_score,
            'enterprising_score': self.enterprising_score, 'investigative_score': self.investigative_score}
        return score_data


class InterestReportMaster(models.Model):
    report_category = models.CharField(max_length=128, choices=Report_Category, default='')
    category_description = models.TextField(default='')
    category_are = models.TextField(default='')
    category_like = models.TextField(default='')
    category_value = models.TextField(default='')
    category_makes = RichTextField(null=True, blank=True, default='')
    category_work = RichTextField(null=True, blank=True, default='')

    def __str__(self):
        return self.report_category


class InterestAnswerData(ModelMixin):
    EXAM_STATUS = (
        ('InProgress', 'InProgress'),
        ('Complete', 'Complete')
    )
    answer = models.CharField(max_length=128, null=True, blank=True, default='')
    exam_status = models.CharField(max_length=30, choices=EXAM_STATUS, default='InProgress')
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager()


class FavoriteCareer(ModelMixin):
    name = models.CharField(max_length=256, null=True, blank=True)
    code = models.CharField(max_length=256, null=True, blank=True)
    link = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        if self.created_by:
            return self.created_by.email
        else:
            return "None"
