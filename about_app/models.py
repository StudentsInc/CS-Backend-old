from django.db import models
from account_app.models import ModelMixin
from ckeditor.fields import RichTextField


class OurAchievementItems(ModelMixin):
    icon = models.ImageField(upload_to='career-studio/about/achievement', blank=True, null=True)
    count = models.CharField(default='16+', max_length=15)
    text = models.CharField(default='Specialists', max_length=150)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Our Achievement Item(s)'
        verbose_name_plural = 'Our Achievement Item(s)'
        ordering = ['-id', ]


class OurAchievement(ModelMixin):
    objects = None
    heading = models.CharField(blank=True, null=True, max_length=255, default='')
    subheading = RichTextField(blank=True, null=True, default='')
    our_achivement_items = models.ManyToManyField(OurAchievementItems, related_name='achievements', blank=True)

    def __str__(self):
        if self.heading:
            return self.heading
        return str(self.id)

    class Meta:
        verbose_name = 'Our Achievement'
        verbose_name_plural = 'Our Achievement'
        ordering = ['-id', ]


class OurTeamItems(ModelMixin):
    name = models.CharField(max_length=255, default='name')
    role = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='career-studio/about/team', blank=True, null=True)
    fb_link = models.CharField(max_length=255, null=True, blank=True)
    tw_link = models.CharField(max_length=255, null=True, blank=True)
    insta_link = models.CharField(max_length=255, null=True, blank=True)
    linked_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Our Team Item(s)'
        verbose_name_plural = 'Our Team Item(s)'
        ordering = ['-id', ]


class OurTeam(ModelMixin):
    objects = None
    heading = models.CharField(blank=True, null=True, max_length=255, default='')
    subheading = RichTextField(blank=True, null=True, default='')
    our_teams = models.ManyToManyField(OurTeamItems, related_name='our_teams',
                                       blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Our Team'
        verbose_name_plural = 'Our Team'
        ordering = ['-id', ]
