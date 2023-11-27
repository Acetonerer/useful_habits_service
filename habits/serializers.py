from rest_framework import serializers

from habits.models import Habit
from habits.validators import (RewardRelaterHabitValidator,
                               TimeCompleteValidator, IsPleaseValidator,
                               CheckValidator)


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [RewardRelaterHabitValidator(
            reward='reward', related_habit='related_habit'),
                      TimeCompleteValidator(time='time_complete'),
                      IsPleaseValidator(related_habit='related_habit'),
                      CheckValidator(is_pleasant='is_pleasant',
                                     reward='reward',
                                     related_habit='related_habit')
                      ]
