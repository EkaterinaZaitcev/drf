from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from materials.models import Course, Lesson, Subscribe
from materials.paginators import MaterialsPaginator
from materials.serializers import (
    CourseDetailSerializer,
    CourseSerializer,
    LessonSerializer,
    SubscribeSerializer,
)
from materials.tasks import send_mail_course_update
from users.permissions import IsModers, IsOwner


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="description from swagger_auto_schema via method_decorator"
    ),
)
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = MaterialsPaginator

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_update(self, serializer):
        course = serializer.save()
        send_mail_course_update.delay(course.id)

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
    """Подписка на курс"""

    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        user = self.request.user
        course_id = self.request.data.get("course")
        course = get_object_or_404(Course, id=course_id)

        subs_item = self.queryset.filter(user=user, course=course)

        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"
        else:
            Subscribe.objects.create(user=user, course=course)
            message = "подписка добавлена"

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
