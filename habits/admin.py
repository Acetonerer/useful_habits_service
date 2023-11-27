from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class AdminHabit(admin.ModelAdmin):
    list_display = ('place', 'action', 'time_start',)
    list_filter = ('is_pleasant',)
