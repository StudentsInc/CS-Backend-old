from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from cms_app.models import *


class MajorSubjectResource(resources.ModelResource):
    class Meta:
        model = MajorSubject
        fields = ('id', 'major', 'subject_name', 'description', 'video')

    def before_save_instance(self, instance, using_transactions, dry_run):
        print(instance)
        print(self, instance, using_transactions, dry_run)
        query = Major.objects.filter(name__icontains=self.major)
        if query:
            return query.id
        return 1


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_title', 'created_by', ]


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_title', 'created_by']


@admin.register(TermsAndCondition)
class TermsAndConditionAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_title', 'created_by']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_by']
    search_fields = ['question']


@admin.register(CareerLibrary)
class CareerLibraryAdmin(admin.ModelAdmin):
    list_display = ['id', 'career_options', 'category', 'name']


@admin.register(CareerLibraryUser)
class CareerLibraryUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_important']


@admin.register(SelectCareer)
class SelectCareerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_by']


@admin.register(CareerVotes)
class CareerVotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'career', 'guest_token']


@admin.register(RecommendationNot)
class RecommendationNotAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_recommendate']


@admin.register(CareerLibraryDetail)
class CareerLibraryDetailAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(SoftSkills)
class SoftSkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(HardSkills)
class HardSkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(WorkValuesScores)
class WorkValueItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


@admin.register(WorkValueItems)
class WorkValueItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


@admin.register(UserWorkValues)
class UserWorkValuesAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


@admin.register(CareerValues)
class CareerValuesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'title', 'data_value']
    list_filter = ['id', 'title']
    search_fields = ['title']


@admin.register(Major)
class MajorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'typical_careers', 'in_demand']
    list_filter = ['id', 'name']
    search_fields = ['name']


@admin.register(UserSelectedMajor)
class MajorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'major', 'created_by']


@admin.register(UserSelectedCareer)
class MajorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'career', 'created_by']


@admin.register(MajorSubject)
class MajorSubjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # resource_class = MajorSubjectResource
    list_display = ['major', 'subject_name']
    search_fields = ['subject_name']
