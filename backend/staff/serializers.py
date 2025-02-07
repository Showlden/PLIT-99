from rest_framework import serializers

from .models import Staff, POSITION

class StaffSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=24, required=True, write_only=True)
    position = serializers.ChoiceField(choices=POSITION)
    phone_number = serializers.CharField(max_length=13)
    email = serializers.EmailField(max_length=255)
    img = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = "id name position img phone_number email".split()

    def get_img(self, obj):
        return obj.img.url