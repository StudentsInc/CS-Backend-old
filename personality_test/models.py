from django.db import models
import numpy as np
from .constants import *
from ckeditor.fields import RichTextField
from account_app.models import ModelMixin, GuestUser

GENDER_TYPE = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
)

QUESTION_TYPE = (
    ('extravert', 'extravert'),
    ('adventurous', 'adventurous'),
    ('agreeable', 'agreeable'),
    ('neurotic', 'neurotic'),
    ('conscientious', 'conscientious'),
)

ANSWER_TYPE = (
    ('strongly_agree', 'strongly_agree'),
    ('agree', 'agree'),
    ('neutral', 'neutral'),
    ('disagree', 'disagree'),
    ('strongly_disagree', 'strongly_disagree'),
)

Key_Type = (
    ('positive', 'positive'),
    ('negative', 'negative')
)

Job_Category = (
    ('high', 1),
    ('mid', 2),
    ('low', 3)
)

Age_Group = (
    ('13-19', '13-19'),
    ('20-24', '20-24'),
    ('25-40', '25-40'),
    ('41-100', '41-100')
)


def chunkify(new_extravert_list, n):
    return [new_extravert_list[i::n] for i in range(n)]


def dashboard_result(list_data, score_data):
    new_list = list(list_data[0])
    new_list.sort(reverse=True)
    split = np.array_split(new_list, 5)
    count = 6
    for array in split:
        count -= 1
        if score_data in array:
            break
    return count


class JobMaster(models.Model):
    objects = None
    title = models.CharField(max_length=256, blank=True)
    category = models.CharField(max_length=100, choices=QUESTION_TYPE)
    job_category = models.CharField(max_length=100, choices=Job_Category)
    date_created = models.DateTimeField(auto_now_add=True)


class EducationLevel(models.Model):
    education = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.education


class Reason(models.Model):
    objects = None
    reason = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.reason


class UserDetail(models.Model):
    gender = models.CharField(max_length=100, choices=GENDER_TYPE, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    educational_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, null=True, blank=True)


class PersonalityDetail(models.Model):
    heading = models.CharField(max_length=300, default="The Big Five Assessment")
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    assesment_button = models.CharField(max_length=300, default="The Big Five Assessment")
    duration = models.IntegerField(null=True, blank=True)
    total_question = models.IntegerField(help_text='Total No of Question', verbose_name='Total No of Question')
    objects = models.Manager()

    def __str__(self):
        return self.heading


class PersonalityQuestion(models.Model):
    personality_detail = models.ForeignKey(PersonalityDetail, on_delete=models.SET_NULL, null=True, blank=True)
    question_type = models.CharField(choices=QUESTION_TYPE, max_length=100, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    key_type = models.CharField(max_length=100, choices=Key_Type, null=True, blank=True)

    def __str__(self):
        return self.question_type


class PersonalityAnswerModel(ModelMixin):
    personality_question = models.ForeignKey(PersonalityQuestion, on_delete=models.CASCADE)
    answer_type = models.CharField(choices=ANSWER_TYPE, max_length=100, null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager()


class PersonalityTest(ModelMixin):
    EXAM_STATUS = (
        ('InProgress', 'InProgress'),
        ('Complete', 'Complete')
    )
    personality_test = models.ManyToManyField(PersonalityAnswerModel, blank=True)
    start_time = models.DateTimeField(auto_now=False, null=True, blank=True)
    end_time = models.DateTimeField(auto_now=False, null=True, blank=True)
    time_left = models.CharField(max_length=100, null=True, blank=True)
    exam_status = models.CharField(max_length=30, choices=EXAM_STATUS, default='InProgress')
    user_detail = models.OneToOneField(UserDetail, on_delete=models.CASCADE, null=True, blank=True)
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager()

    def get_age(self):
        age_range = 0
        if 13 <= int(self.user_detail.age) <= 19:
            age_range = '13-19'
        if 20 <= int(self.user_detail.age) <= 24:
            age_range = '20-24'
        if 25 <= int(self.user_detail.age) <= 40:
            age_range = '25-40'
        if 40 <= int(self.user_detail.age) <= 100:
            age_range = '40-100'
        return age_range

    def user_scores(self):
        extravert_list = []
        adventurous_list = []
        agreeable_list = []
        neurotic_list = []
        conscientious_list = []
        for i in self.personality_test.all():
            if i.personality_question.question_type == 'extravert':
                extravert_list.append(i.score)
            if i.personality_question.question_type == 'adventurous':
                adventurous_list.append(i.score)
            if i.personality_question.question_type == 'agreeable':
                agreeable_list.append(i.score)
            if i.personality_question.question_type == 'neurotic':
                neurotic_list.append(i.score)
            if i.personality_question.question_type == 'conscientious':
                conscientious_list.append(i.score)
        extravert_score, adventurous_score = sum(extravert_list), sum(adventurous_list)
        agreeable_score, neurotic_score = sum(agreeable_list), sum(neurotic_list)
        conscientious_score = sum(conscientious_list)
        ctx = {'extravert_score': extravert_score,
               'adventurous_score': adventurous_score,
               'agreeable_score': agreeable_score,
               'neurotic_score': neurotic_score,
               'conscientious_score': conscientious_score}
        return ctx

    def dashboard_data(self):
        score_data = self.user_scores()
        extravert_scores_list = []
        adventurous_scores_list = []
        agreeable_scores_list = []
        neurotic_scores_list = []
        conscientious_scores_list = []

        extravert_dashboard = UserAssesmentStats.objects.all().values_list('extravert_score', flat=True)
        extravert_scores_list.append(extravert_dashboard)
        extravert_result = dashboard_result(list_data=extravert_scores_list, score_data=score_data['extravert_score'])
        extravert_dashboard_result = extravert_constant[extravert_result]

        adventurous_dashboard = UserAssesmentStats.objects.all().values_list('adventurous_score', flat=True)
        adventurous_scores_list.append(adventurous_dashboard)
        adventurous_result = dashboard_result(list_data=adventurous_scores_list,
                                              score_data=score_data['adventurous_score'])
        adventurous_dashboard_result = adventurous_constant[adventurous_result]

        agreeable_dashboard = UserAssesmentStats.objects.all().values_list('agreeable_score', flat=True)
        agreeable_scores_list.append(agreeable_dashboard)
        agreeable_result = dashboard_result(list_data=agreeable_scores_list, score_data=score_data['agreeable_score'])
        agreeable_dashboard_result = agreeable_constant[agreeable_result]

        neurotic_dashboard = UserAssesmentStats.objects.all().values_list('neurotic_score', flat=True)
        neurotic_scores_list.append(neurotic_dashboard)
        neurotic_result = dashboard_result(list_data=neurotic_scores_list, score_data=score_data['neurotic_score'])
        neurotic_dashboard_result = neurotic_constant[neurotic_result]

        conscientious_dashboard = UserAssesmentStats.objects.all().values_list('conscientious_score', flat=True)
        conscientious_scores_list.append(conscientious_dashboard)
        conscientious_result = dashboard_result(list_data=conscientious_scores_list,
                                                score_data=score_data['conscientious_score'])
        conscientious_dashboard_result = conscientious_constant[conscientious_result]

        ctx = {
            'extravert_score': extravert_result, 'adventurous_score': adventurous_result,
            'agreeable_score': agreeable_result, 'neurotic_score': neurotic_result,
            'conscientious_score': conscientious_result,
            'extravert_dashboard': extravert_dashboard_result, 'adventurous_dashboard': adventurous_dashboard_result,
            'agreeable_dashboard': agreeable_dashboard_result, 'neurotic_dashboard': neurotic_dashboard_result,
            'conscientious_dashboard': conscientious_dashboard_result
        }
        return ctx

    def assessment_stats_save(self):
        age_data = self.get_age()
        current_user = self.user_scores()
        extravert_stats = AssessmentStats.objects.filter(age_group=age_data, assesment_category='extravert')
        if extravert_stats:
            user_count, total_score = extravert_stats.last().user_count, extravert_stats.last().total_score
            extravert_stats.update(user_count=user_count + 1, total_score=total_score + current_user['extravert_score'])
        else:
            AssessmentStats.objects.create(age_group=age_data, assesment_category='extravert', user_count=1,
                                           total_score=current_user['extravert_score'])

        adventurous_stats = AssessmentStats.objects.filter(age_group=age_data, assesment_category='adventurous')
        if adventurous_stats:
            user_count, total_score = adventurous_stats.last().user_count, adventurous_stats.last().total_score
            adventurous_stats.update(user_count=user_count + 1,
                                     total_score=total_score + current_user['adventurous_score'])
        else:
            AssessmentStats.objects.create(age_group=age_data, assesment_category='adventurous', user_count=1,
                                           total_score=current_user['adventurous_score'])

        agreeable_stats = AssessmentStats.objects.filter(age_group=age_data, assesment_category='agreeable')
        if agreeable_stats:
            user_count, total_score = agreeable_stats.last().user_count, agreeable_stats.last().total_score
            agreeable_stats.update(user_count=user_count + 1, total_score=total_score + current_user['agreeable_score'])
        else:
            AssessmentStats.objects.create(age_group=age_data, assesment_category='agreeable', user_count=1,
                                           total_score=current_user['agreeable_score'])

        neurotic_stats = AssessmentStats.objects.filter(age_group=age_data, assesment_category='neurotic')
        if neurotic_stats:
            user_count, total_score = neurotic_stats.last().user_count, neurotic_stats.last().total_score
            neurotic_stats.update(user_count=user_count + 1, total_score=total_score + current_user['neurotic_score'])
        else:
            AssessmentStats.objects.create(age_group=age_data, assesment_category='neurotic', user_count=1,
                                           total_score=current_user['neurotic_score'])

        conscientious_stats = AssessmentStats.objects.filter(age_group=age_data, assesment_category='conscientious')
        if conscientious_stats:
            user_count, total_score = conscientious_stats.last().user_count, conscientious_stats.last().total_score
            neurotic_stats.update(user_count=user_count + 1,
                                  total_score=total_score + current_user['conscientious_score'])
        else:
            AssessmentStats.objects.create(age_group=age_data, assesment_category='conscientious', user_count=1,
                                           total_score=current_user['conscientious_score'])
        return {'message': 'Assessment_data created and updated'}

    def all_user_data(self):
        age_group = self.get_age()
        extravert_score = AssessmentStats.objects.get(age_group=age_group, assesment_category='extravert')
        extravert_average = round(extravert_score.total_score / extravert_score.user_count)

        adventurous_score = AssessmentStats.objects.get(age_group=age_group, assesment_category='adventurous')
        adventurous_average = round(adventurous_score.total_score / adventurous_score.user_count)

        agreeable_score = AssessmentStats.objects.get(age_group=age_group, assesment_category='agreeable')
        agreeable_average = round(agreeable_score.total_score / agreeable_score.user_count)

        neurotic_score = AssessmentStats.objects.get(age_group=age_group, assesment_category='neurotic')
        neurotic_average = round(neurotic_score.total_score / neurotic_score.user_count)

        conscientious_score = AssessmentStats.objects.get(age_group=age_group, assesment_category='conscientious')
        conscientious_average = round(conscientious_score.total_score / conscientious_score.user_count)

        extravert_user_score, adventurous_user_score = extravert_average, adventurous_average
        agreeable_user_score, neurotic_user_score = agreeable_average, neurotic_average
        conscientious_user_score = conscientious_average
        extravert_high, extravert_low = (round(float(extravert_user_score + 5))), (
            round(float(extravert_user_score - 5)))
        extravert_mid = extravert_user_score

        adventurous_high, adventurous_low = (round(float(adventurous_user_score + 5))), (
            round(float(adventurous_user_score - 5)))
        adventurous_mid = adventurous_user_score

        agreeable_high, agreeable_low = (round(float(agreeable_user_score + 5))), (
            round(float(agreeable_user_score - 5)))
        agreeable_mid = agreeable_user_score

        neurotic_high, neurotic_low = (round(float(neurotic_user_score + 5))), (round(float(neurotic_user_score - 5)))
        neurotic_mid = neurotic_user_score

        conscientious_high, conscientious_low = (round(float(conscientious_user_score + 5))), (
            round(float(conscientious_user_score - 5)))
        conscientious_mid = conscientious_user_score
        ctx = {'extravert_high': extravert_high, 'extravert_low': extravert_low, 'extravert_mid': extravert_mid,
               'adventurous_high': adventurous_high, 'adventurous_low': adventurous_low,
               'adventurous_mid': adventurous_mid,
               'agreeable_high': agreeable_high, 'agreeable_low': agreeable_low,
               'agreeable_mid': agreeable_mid,
               'neurotic_high': neurotic_high, 'neurotic_low': neurotic_low,
               'neurotic_mid': neurotic_mid,
               'conscientious_high': conscientious_high, 'conscientious_low': conscientious_low,
               'conscientious_mid': conscientious_mid
               }
        return ctx

    def status_type(self):
        current_user = self.user_scores()
        all_users = self.all_user_data()
        extravert_status = None
        adventurous_status = None
        agreeable_status = None
        neurotic_status = None
        conscientious_status = None
        if current_user['extravert_score'] < all_users['extravert_low']:
            extravert_status = 'low'
        if current_user['extravert_score'] > all_users['extravert_high']:
            extravert_status = 'high'
        if all_users['extravert_low'] < current_user['extravert_score'] < all_users['extravert_high']:
            extravert_status = 'mid'
        if current_user['adventurous_score'] < all_users['adventurous_low']:
            adventurous_status = 'low'
        if current_user['adventurous_score'] > all_users['adventurous_high']:
            adventurous_status = 'high'
        if all_users['adventurous_low'] < current_user['adventurous_score'] < all_users['adventurous_high']:
            adventurous_status = 'mid'
        if current_user['agreeable_score'] < all_users['agreeable_low']:
            agreeable_status = 'low'
        if current_user['agreeable_score'] > all_users['agreeable_high']:
            agreeable_status = 'high'
        if all_users['agreeable_low'] < current_user['agreeable_score'] < all_users['agreeable_high']:
            agreeable_status = 'mid'
        if current_user['neurotic_score'] < all_users['neurotic_low']:
            neurotic_status = 'low'
        if current_user['neurotic_score'] > all_users['neurotic_high']:
            neurotic_status = 'high'
        if all_users['neurotic_low'] < current_user['neurotic_score'] < all_users['neurotic_high']:
            neurotic_status = 'mid'
        if current_user['conscientious_score'] < all_users['conscientious_low']:
            conscientious_status = 'low'
        if current_user['conscientious_score'] > all_users['conscientious_high']:
            conscientious_status = 'high'
        if all_users['conscientious_low'] < current_user['conscientious_score'] < all_users['conscientious_high']:
            conscientious_status = 'mid'
        ctx = {
            'extravert_status': extravert_status,
            'adventurous_status': adventurous_status,
            'agreeable_status': agreeable_status,
            'neurotic_status': neurotic_status,
            'conscientious_status': conscientious_status,
        }
        return ctx


class AssessmentStats(models.Model):
    """
    This models contains the user count of all the users taken the personality test and scores by them with age group
    """
    user_count = models.PositiveIntegerField(default=0)
    total_score = models.PositiveIntegerField(default=0)
    age_group = models.CharField(max_length=100, choices=Age_Group, null=True, blank=True)
    assesment_category = models.CharField(max_length=100, choices=QUESTION_TYPE, null=True, blank=True)


class UserAssesmentStats(ModelMixin):
    """
    This model contains all categories score calculated by the exam given of personality test and saved the scores
    with ranging high , mid and low
    """
    assesment = models.ForeignKey(PersonalityTest, on_delete=models.CASCADE, null=True, blank=True)
    extravert = models.CharField(max_length=100, null=True, blank=True)
    extravert_score = models.PositiveIntegerField(default=0)
    adventurous = models.CharField(max_length=100, null=True, blank=True)
    adventurous_score = models.PositiveIntegerField(default=0)
    agreeable = models.CharField(max_length=100, null=True, blank=True)
    agreeable_score = models.PositiveIntegerField(default=0)
    neurotic = models.CharField(max_length=100, null=True, blank=True)
    neurotic_score = models.PositiveIntegerField(default=0)
    conscientious = models.CharField(max_length=100, null=True, blank=True)
    conscientious_score = models.PositiveIntegerField(default=0)
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.created_by.email


class PersonalityDashboard(ModelMixin):
    """
    This model contains all categories score calculated via all other users score and scaled according to the
    scored calculated
    """
    extravert_scale = models.CharField(max_length=128, null=True, blank=True)
    extravert_score = models.PositiveIntegerField(default=0)
    adventurous_scale = models.CharField(max_length=128, null=True, blank=True)
    adventurous_score = models.PositiveIntegerField(default=0)
    agreeable_scale = models.CharField(max_length=128, null=True, blank=True)
    agreeable_score = models.PositiveIntegerField(default=0)
    neurotic_scale = models.CharField(max_length=128, null=True, blank=True)
    neurotic_score = models.PositiveIntegerField(default=0)
    conscientious_scale = models.CharField(max_length=128, null=True, blank=True)
    conscientious_score = models.PositiveIntegerField(default=0)
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.created_by.email


class PersonalityReportMaster(models.Model):
    """
    This is a master data for personality test report consisting category and score.
    """
    category = models.CharField(max_length=128, choices=QUESTION_TYPE)
    category_description = RichTextField(blank=True, null=True, default='')
    category_detail = models.TextField(default='')
    score = models.CharField(max_length=128, choices=Job_Category)
    score_description = RichTextField(blank=True, null=True, default='')
    strength = RichTextField(blank=True, null=True, default='')
    weakness = RichTextField(blank=True, null=True, default='')

    def __str__(self):
        return self.category

