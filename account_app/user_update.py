from account_app.models import *
from interest_app.models import *
from personality_test.models import *


def user_update(token, user):
    query = GuestUser.objects.filter(token=token).update(user=user)
    interest_answer = AnswerModel.objects.filter(guest_user__token=token)
    if interest_answer:
        interest_answer.update(created_by=user, updated_by=user)
    user_interest_test = UserInterestTest.objects.filter(guest_user__token=token)
    if user_interest_test:
        user_interest_test.update(created_by=user, updated_by=user)
    user_score = UserScores.objects.filter(guest_user__token=token)
    if user_score:
        user_score.update(created_by=user, updated_by=user)
    personality_answer = PersonalityAnswerModel.objects.filter(guest_user__token=token)
    if personality_answer:
        personality_answer.update(created_by=user, updated_by=user)
    personality_test = PersonalityTest.objects.filter(guest_user__token=token)
    if personality_test:
        personality_test.update(created_by=user, updated_by=user)
    user_assessment_stats = UserAssesmentStats.objects.filter(guest_user__token=token)
    if user_assessment_stats:
        user_assessment_stats.update(created_by=user, updated_by=user)
    personality_dashboard = PersonalityDashboard.objects.filter(guest_user__token=token)
    if personality_dashboard:
        personality_dashboard.update(created_by=user, updated_by=user)
    interest_answer_data = InterestAnswerData.objects.filter(guest_user__token=token)
    if interest_answer_data:
        interest_answer_data.update(created_by=user, updated_by=user)
    return "User Updated"
