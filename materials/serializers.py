from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from materials.models import Course, Lesson, Subscribe
from materials.validators import URLValidator


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(validators=[URLValidator])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    subscribe = SerializerMethodField()

    def get_number_of_lessons(self, obj):
        return obj.lessons.count()

    def get_subscribe(self, obj):
        return True if Subscribe.objects.filters(user=self.context["request"].user, course=obj.pk) else False

    class Meta:
        model = Course
        fields = ["id", "name", "picture", "description", "owner", "number_of_lessons", "lessons"]


class SubscribeSerializer(serializers.ModelSerializer):
    """Сериализатор подписки на курс"""

    class Meta:
        model = Subscribe
        fields = ["course"]
