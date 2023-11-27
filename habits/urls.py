from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (PublicHabitList, HabitUpdate,
                          HabitDelete, HabitDetail, HabitCreateView, HabitList)

app_name = HabitsConfig.name

urlpatterns = [
    path('', PublicHabitList.as_view(), name='public_list'),
    path('create/', HabitCreateView.as_view(), name='create'),
    path('update/<int:pk>/', HabitUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', HabitDelete.as_view(), name='delete'),
    path('list/', HabitList.as_view(), name='owner_list'),
    path('detail/<int:pk>/', HabitDetail.as_view(), name='detail'),
]
