from .models import BLOG
from rest_framework import serializers

class BLOGSerializers(serializers.ModelSerializer):
    class Meta:
        model=BLOG
        fields='__all__'