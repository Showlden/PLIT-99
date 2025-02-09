from rest_framework import serializers

from .models import Specialization, Course

class BaseImageSerializer(serializers.ModelSerializer):
    preview_img = serializers.ImageField(read_only=True)
    banner_img = serializers.ImageField(read_only=True)

class SpecializationSerializer(BaseImageSerializer):
    class Meta:
        model = Specialization
        fields = "id title description term contract preview_img banner_img".split()

class CourseSerializer(BaseImageSerializer):
    class Meta:
        model = Course
        fields = "id title description term price preview_img banner_img".split()
