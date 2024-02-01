from django.shortcuts import render
from user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer, LoginSerializer
from rest_framework import status

class UserSignupView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        try:
            User.objects.get(email=email)
            return Response('Email already exists')
        except User.DoesNotExist:
            serializer = UserSerializer(data=request.data, context = {"request": request})
            if serializer.is_valid():
                user = serializer.save()
                user.set_password(request.data.get('password'))
                user.save()
                serializer_data = {'message': 'Register Successfully', 'data': serializer.data}
                return Response(serializer_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data.get("email")
            password = request.data.get("password")

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
            
            if user.check_password(password):
                return Response("Login Successful", status=status.HTTP_200_OK)
            
            else:
                return Response("Invaild Password", status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

