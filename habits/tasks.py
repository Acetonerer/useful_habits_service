from config.celery import shared_task
from django.conf import settings
from habits.models import Habit
import requests


@shared_task
def send_message_telegram(habit_id):
    bot_api_key = settings.API_TELEGRAM
    habit = Habit.objects.get(id=habit_id)
    chat_id = habit.owner.chat_id
    message = f"Я буду {habit.action} в {habit.place} в {habit.time_start}"
    params = {'chat_id': chat_id, 'text': message}
    requests.post(f'https://api.telegram.org/bot{bot_api_key}/sendMessage', params=params)
