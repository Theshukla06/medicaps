from rest_framework import serializers
from user.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("id", "first_name", "last_name", "email", "mobile_no", "password")
        extra_kwargs = {
            "email": {"validators": []},
            "first_name": {"required": True},
            "last_name": {"required": True}
        }

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = User
        fields = ['email', 'password'] 
     
    def validate(self, attrs):
        email = attrs.get("email", "")
         
        if email == "":
            raise serializers.ValidationError("Email is required")
            
        return super().validate(attrs)