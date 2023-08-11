from django.db import models

# Create your models here.
from account_app.models import ModelMixin

Survey_Answer = (
    ('agree', 'agree'),
    ('disagree', 'disagree')
)


class SurveyQuestion(models.Model):
    question = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question


class UserSurvey(ModelMixin):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, null=True, blank=True)
    answer_type = models.CharField(max_length=100, choices=Survey_Answer, null=True, blank=True)
    answer_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question.question
