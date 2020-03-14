from django.contrib.auth.models import User
from django.db import models

DEFAULT_STATUS_ID = 1
DEFAULT_TYPE_ID = 1
PROJECT_DEFAULT_STATUS = 'public'
PROJECT_STATUS_CHOICES = [
    ('public', 'Общий'),
    ('hidden', 'Скрытый'),
    ('private', 'Приватный')
]


class File(models.Model):
    signature = models.CharField(max_length=50, verbose_name='Подпись')
    upload = models.FileField(upload_to='uploads/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='Автор', related_name='created_file')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=50, verbose_name='Статус', default=PROJECT_DEFAULT_STATUS,
                              choices=PROJECT_STATUS_CHOICES)
