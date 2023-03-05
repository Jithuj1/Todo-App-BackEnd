from rest_framework import serializers
from .models import Today

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Today
        fields = "__all__"
    




