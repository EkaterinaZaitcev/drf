from rest_framework import generics, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from materials.models import Course, Lesson, Subscribe
from materials.paginators import MaterialsPaginator
from materials.serializers import CourseDetailSerializer, CourseSerializer, LessonSerializer, SubscribeSerializer
from users.permissions import IsModers, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = MaterialsPaginator

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated, ~IsModers)
        elif self.action == "destroy":
            self.permission_classes = (~IsModers | IsOwner,)
        else:
            self.permission_classes = (IsModers | IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        if not IsModers().has_permission(self.request, self):
            return Course.objects.filter(owner=self.request.user)
        return Course.objects.all()


class CourseSubscribeApiView(views.APIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.kwargs.get("pk")
        course_item = get_object_or_404 (Course, pk=course_id)

        subs_item =self.request.data.get("course")

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscribe.objects.create(user=user, course=course_item, )
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response({"message": message})


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, ~IsModers)
    pagination_class = MaterialsPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModers | IsOwner)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModers | IsOwner)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | ~IsModers)
