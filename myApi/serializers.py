from rest_framework import serializers

from myApi.models import gallery


class gallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = gallery
        fields = ('pk','title', 'image', 'thumbnail',)
        read_only_fields = ('thumbnail',)
