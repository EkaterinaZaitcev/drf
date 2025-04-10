from http.client import responses
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscribe
from users.models import CustomUser


class MaterialsTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='test@yandex.ru',)
        self.course = Course.objects.create(name='1 Course',
                                            description='First course',
                                            owner=self.user)
        self.lesson = Lesson.objects.create(name='Lesson 1',
                                            course=self.course,
                                            description='This is lesson 1',
                                            video_link='http://www.youtube.com',
                                            owner=self.user)
        self.subscribe = Subscribe(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson-detail', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), self.lesson.name)

    def test_lesson_create(self):
        url = reverse('materials:lesson-create')
        data = {
            "name":'Lesson 1',
            "description":'This is lesson 1',
            "course":self.course.pk,
            "video_link":'http://www.youtube.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {"id":2, "name":"Lesson 1",
                                            "course":1,
                                            "description":'This is lesson 1',
                                            "preview": None,
                                            "video_link" : 'http://www.youtube.com',
                                            "owner":1}
                         )
    def test_lesson_update(self):
        url = reverse('materials:lesson-update', args=(self.lesson.pk,))
        data = {
            "name": 'Lesson 2',
            "description": 'This is lesson 2',
            }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"id": 4, "name": "Lesson 2",
                                           "course": 3,
                                           "description": 'This is lesson 2',
                                           "preview": None,
                                           "video_link": 'http://www.youtube.com',
                                           "owner": 3}
                         )

class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email='test@yandex.ru',)
        self.course = Course.objects.create(name='1 Course',
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_subscribe(self):
        url = reverse('materials:subscribe', args=(self.course.pk,))
        body = {"subscribe": True}
        request = self.client.post(url, body)
        response = request.json()
        print(response)
        print(response.status_code)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get("message"), "подписка добавлена")
