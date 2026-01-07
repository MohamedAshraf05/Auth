from django.shortcuts import render
from rest_framework import generics , permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer , UserProfileSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser , UserProfile
# Create your views here.


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

# display data  , create data
class UserProfileApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self , request):
        user = request.user

        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return Response({"message" : "Profile not exists"} , status=404)

        serializer = UserProfileSerializer(profile)
        return Response(serializer.data , status=200)   
    
    def post(self , request):
        user = request.user
        data = request.data.copy()

        data["user"] = user.pk

        serializer = UserProfileSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        return Response(serializer.errors , status=400)



        