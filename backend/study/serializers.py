from rest_framework import serializers

from .models import Specialization, Course

from rest_framework import serializers

class SpecializationSerializer(serializers.ModelSerializer):
    preview_img_url = serializers.ImageField(source="preview_img", read_only=True)
    banner_img_url = serializers.ImageField(source="banner_img", read_only=True)

    class Meta:
        model = Specialization
        fields = "id title description term contract preview_img_url banner_img_url".split()


class CourseSerializer(serializers.ModelSerializer):
    preview_img_url = serializers.ImageField(source="preview_img", read_only=True)
    banner_img_url = serializers.ImageField(source="banner_img", read_only=True)

    class Meta:
        model = Course
        fields = "id title description term price preview_img_url banner_img_url".split()