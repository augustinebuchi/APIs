from rest_restframework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        field = ['id', 'name', 'order']