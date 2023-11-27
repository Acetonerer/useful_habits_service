from rest_framework import serializers


class RewardRelaterHabitValidator:
    def __init__(self, reward, related_habit):
        self.reward = reward
        self.related_habit = related_habit

    def __call__(self, value):
        reward_habit = dict(value).get(self.reward)
        related = dict(value).get(self.related_habit)
        if reward_habit and related:
            raise serializers.ValidationError('Выберите только одно условие:'
                                              ' или награда, '
                                              'или полезная привычка')


class TimeCompleteValidator:
    def __init__(self, time):
        self.time_complete = time

    def __call__(self, value):
        time_comp = value.get(self.time_complete)
        if time_comp > 100:
            raise serializers.ValidationError(
                'Время выполнения не может быть более 100 секунд')


class IsPleaseValidator:
    def __init__(self, related_habit):
        self.related_habit = related_habit

    def __call__(self, value):
        habit = dict(value).get(self.related_habit)

        if 'related_habit' in value:
            if not habit.is_pleasant:
                raise serializers.ValidationError(
                    'Связанная привычка должна быть полезной')


class CheckValidator:
    def __init__(self, is_pleasant, reward, related_habit):
        self.is_pleasant = is_pleasant
        self.reward = reward
        self.related_habit = related_habit

    def __call__(self, value):
        nice = dict(value).get(self.is_pleasant)
        reward_habit = dict(value).get(self.reward)
        related = dict(value).get(self.related_habit)
        if nice:
            if reward_habit or related:
                raise serializers.ValidationError(
                    'У полезной привычки не может быть награды'
                    ' или связанной привычки')
