from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscribe
from users.models import CustomUser


class MaterialsTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='test', email='test@yandex.ru', password='1234qwerty')
        self.course = Course.objects.create(name='1 Course',
                                            description='First course',
                                            owner=self.user)
        self.lesson = Lesson.objects.create(name='Lesson 1',
                                            course=self.course,
                                            description='This is lesson 1',
                                            video_link='http://youtube.com')
        self.subscribe = Subscribe(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson-detail', args=(self.lesson.pk, ))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), self.lesson.name)



