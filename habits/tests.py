from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test')
        self.client.force_authenticate(user=self.user)
        self.user.set_password('test123')
        self.user.save()

        self.habit = Habit.objects.create(
            place='test',
            time_start='10:00',
            action='testov',
            periodicity=1,
            reward='test testes',
            time_complete=120,
            owner=self.user
        )

    def test_create_habit(self):
        """Тестирование создания привычки"""

        data = {
            'place': 'место',
            'time_start': '08:00:00',
            'action': 'почистить зубы коту',
            'periodicity': '1',
            'reward': 'скушать яблоко',
            'time_complete': 120,
            'owner': self.user.id
        }
        response = self.client.post('/habit/create/', data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_list_habit(self):
        """Тестирование вывода списка привычек"""
        response = self.client.get('/habit/list/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertTrue(Habit.objects.all().exists())

    def test_update_habit(self):
        data = {
            'place': 'test место',
            'time_start': '10:00',
            'action': 'почистить зубы коту',
            'periodicity': 1,
            'reward': 'скушать яблоко',
            'time_complete': 120,
            'owner': self.user.id
        }

        response = self.client.put(f'/habit/update/{self.habit.id}/',
                                   data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_partial_update_habit(self):
        data = {
            'place': 'testovoe',
            'time_complete': 120,
            'periodicity': 1
        }

        response = self.client.patch(f'/habit/update/{self.habit.id}/',
                                     data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_detail_habit(self):
        response = self.client.get(f'/habit/detail/{self.habit.id}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'id': self.habit.id, 'place': 'test', 'time_start': '10:00:00',
             'action': 'testov', 'is_pleasant': False, 'periodicity': '1',
             'reward': 'test testes', 'time_complete': 120,
             'is_published': False, 'owner': self.user.id,
             'related_habit': None}
        )

    def test_delete_habit(self):
        response = self.client.delete(f'/habit/delete/{self.habit.id}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertTrue(not Habit.objects.all().exists())
