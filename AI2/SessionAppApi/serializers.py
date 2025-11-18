from rest_framework import serializers
from SessionApp.models import SESSION
class SessionSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = SESSION
        fields = '__all__'

