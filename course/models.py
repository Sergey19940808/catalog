# Imports
import django.utils.timezone
from django.db import models


# Create model for course
class Course(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=u'Имя курса:')
    description = models.TextField(verbose_name=u'Описание курса:')
    date_added = models.DateTimeField(default=django.utils.timezone.now, verbose_name=u'Дата публикации курса:')

    def __str__(self):
        return self.name
