from django.db import models
from account_app.models import ModelMixin


# Create your models here.
class LearningQuestion(models.Model):
    heading = models.CharField(max_length=300, null=True, blank=True)
    question_no = models.IntegerField(verbose_name='Question No')
    image = models.FileField(null=True, blank=True)
    question = models.TextField(default='')
    option_1 = models.CharField(max_length=150, null=True, blank=True)
    option_2 = models.CharField(max_length=150, null=True, blank=True)
    option_3 = models.CharField(max_length=150, null=True, blank=True)
    option_4 = models.CharField(max_length=150, null=True, blank=True)
    option_5 = models.CharField(max_length=150, null=True, blank=True)
    objects = models.Manager()

    class Meta:
        ordering = ['question_no', ]


class LearningAnswerModel(ModelMixin):
    question_detail = models.ForeignKey(LearningQuestion, on_delete=models.CASCADE)
    answer = models.CharField(help_text='like(1) to dislike(5)',
                              max_length=10)

    def __str__(self):
        return str(self.answer)


class LearningUserInterestTest(ModelMixin):
    EXAM_STATUS = (
        ('InProgress', 'InProgress'),
        ('Complete', 'Complete')
    )
    answer = models.ManyToManyField(LearningAnswerModel, blank=True)
    start_time = models.DateTimeField(auto_now=False, null=True, blank=True)
    end_time = models.DateTimeField(auto_now=False, null=True, blank=True)
    exam_status = models.CharField(max_length=30, choices=EXAM_STATUS, default='InProgress')
    objects = models.Manager()

    def __str__(self):
        return self.exam_status
