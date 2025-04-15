from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

from materials.models import Course, Lesson, Subscribe
from materials.validators import url_validator


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(validators=[url_validator])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    subscribe = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        return course.lessons.count()

    def get_subscribe(self, course):
        current_user = self.context.get("request", None).user
        return course.course_subscription.filter(user=current_user).exists()

    class Meta:
        model = Course
        fields = "__all__"


class SubscribeSerializer(serializers.ModelSerializer):
    """Сериализатор подписки на курс"""

    class Meta:
        model = Subscribe
        fields = ["course"]
