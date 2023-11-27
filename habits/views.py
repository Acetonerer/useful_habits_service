from django_celery_beat.models import PeriodicTask
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializers
from habits.services import create_periodic_task
from users.permissions import IsOwner


class HabitCreateView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        create_periodic_task(new_habit)
        new_habit.save()


class HabitUpdate(generics.UpdateAPIView):
    """Редактирование привычки"""
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        habit = serializer.save()
        task = PeriodicTask.objects.get(args__contains=[habit.id])
        if task:
            task.delete()
        create_periodic_task(habit)


class HabitDelete(generics.DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitList(generics.ListAPIView):
    """Просмотр привычек пользователя"""
    serializer_class = HabitSerializers
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Habit.objects.filter(owner=self.request.user).order_by('pk')
        return queryset


class HabitDetail(generics.RetrieveAPIView):
    """Просмотр детальной информации по привычке"""
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitList(generics.ListAPIView):
    """Просмотр публичных привычек"""
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated]
