from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import URLValidator


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    video_link = serializers.URLField(validators=[URLValidator()])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_number_of_lessons(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ["id", "name", "picture", "description", "owner", "number_of_lessons", "lessons"]
