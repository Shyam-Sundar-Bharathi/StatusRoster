from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .serializers import ClusterSerializer, MemberSerializer, LoginSerializer, RosterSerializer, ResetPasswordSerializer, StatusSerializer
from .models import Cluster, Member, Roster, Status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .signals import create_log
from django.contrib.auth.hashers import make_password

def index(request):
    return HttpResponse('<h1>Namaskara</h1>')

class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return Response({'status': True, 'message': 'Login successful'})
            else:
                return Response({'status': False, 'error': 'Invalid credentials'}, status=401)
        else:
            return Response({'status': False, 'error': 'Invalid data'}, status=400)


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        print('Perform create called in MemberViewSet')
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        print('Token created')
        return Response({'message': 'User created successfully', 'token': token.key}, status=status.HTTP_201_CREATED)

class ClusterViewSet(viewsets.ModelViewSet):
    serializer_class = ClusterSerializer
    queryset = Cluster.objects.all()

class RosterViewSet(viewsets.ModelViewSet):
    serializer_class = RosterSerializer
    queryset = Roster.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        user = self.request.user  # Get authenticated user
        serializer.save()
        create_log(sender=Roster, instance=serializer.instance, created=True, user=user)


class ResetPasswordView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            confirm_password = serializer.validated_data['confirm_password']
            if password != confirm_password:
                return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Get the user based on the authentication
            user = request.user
            # If you want to allow password reset via email, you can include logic here
            # to retrieve the user based on an email address or token
            
            # Reset the user's password
            user.password = make_password(password)
            user.save()
            return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()