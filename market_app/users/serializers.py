from typing import Any, Dict
from rest_framework_simplejwt import serializers


class CustomTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    """
    Custom serializer for return only access jwt token without refresh token.
    """
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
            data = super().validate(attrs)
            data.pop('refresh', None) 
            return data