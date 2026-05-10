from django.shortcuts import render
from rest_framework import generics , permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer , UserSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser , UserProfile
# Create your views here.


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class UserProfileView(APIView):
    def get(self, request):
        user_profile = CustomUser.objects.get(id=request.user.id)
        serializer = UserSerializer(user_profile)
        return Response(serializer.data)

        