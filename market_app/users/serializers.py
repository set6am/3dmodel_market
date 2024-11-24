from typing import Any, Dict
from rest_framework_simplejwt import serializers


class CustomTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
            data = super().validate(attrs)
            data.pop('refresh', None)  # delete refresh token, only access token return
            return data