from rest_framework.serializers import ModelSerializer
from ads.models import City , Category , Ad

class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'