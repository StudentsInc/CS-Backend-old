from django.db import models


class LanguageManager(models.Manager):
    """
      this manager is used to filter default language type data
    """

    def get_queryset(self):
        print(self)
        return super().get_queryset().filter(language_code='en')

        chat_users = Message.objects.filter(Q(user=user) | Q(created_by=user), is_read=False)
        chat_created_id =  chat_users.values_list('created_by', flat=True)
        chat_user_id = chat_users.values_list('user', flat=True)
        message_user = list(set(chat_user_id+chat_created_id))

