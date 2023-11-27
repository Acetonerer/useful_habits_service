from django.db import models
from config import settings
NULLABLE = {'blank': True, 'null': True}
PERIODICITY_CHOICES = (
    ('1', 'раз в 7 дней'),
    ('2', '2 раза в 7 дней'),
    ('3', '3 раза в 7 дней'),
    ('4', '4 раза в 7 дней'),
    ('5', '5 раз в 7 дней'),
    ('6', '6 раз в 7 дней'),
    ('7', '7 раз в 7 дней')
)


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=50, verbose_name='Место')
    time_start = models.TimeField(verbose_name='Время выполнения привычки')
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False,
                                      verbose_name='Полезная привычка')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE,
                                      verbose_name='Связанная привычка',
                                      **NULLABLE)
    periodicity = models.CharField(max_length=10, choices=PERIODICITY_CHOICES,
                                   default=1,
                                   verbose_name='Частота в неделю',
                                   **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение',
                              **NULLABLE)
    time_complete = models.IntegerField(
        verbose_name='Время на выполнение в сек')
    is_published = models.BooleanField(default=False,
                                       verbose_name='Опубликована',
                                       **NULLABLE)

    def __str__(self):
        return f'{self.action} в {self.time_start} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
