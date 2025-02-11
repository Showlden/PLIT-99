from rest_framework import serializers

from .models import News, NewsImage, NEWS_TYPES

class NewsSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=NEWS_TYPES)
    imgs = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "id title description date type is_pinned imgs".split()

    def get_imgs(self, obj):
        related_images = NewsImage.objects.filter(news=obj)
        return [img.image.url for img in related_images if img.image]
