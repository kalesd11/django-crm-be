from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .models import Subscription, Card, Address, Bill, Customer, Lead, Project
from .serializers import (
    SubscriptionSerializer, CardSerializer, AddressSerializer, BillSerializer,
    CustomerSerializer, LeadSerializer, ProjectSerializer
)

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
            return Response(
                {"error": "Please provide both username and password"},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    # Authenticate user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        django_login(request, user)
        if user.is_superuser:
                role = "Admin"
        elif user.is_staff:
                role = "Staff"
        else:
                role = "User"
            
        user_data = {
                "userId": user.id,
                "username": user.username,
                "email": user.email,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "role": role,
                "isAuthenticated": True
            }
            
        return Response(user_data, status=status.HTTP_200_OK)
    else:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

@api_view(["GET"])
@permission_classes([AllowAny])
@csrf_exempt
def logout(request):
    """
    Logout user and clear session
    Can be called with or without username parameter
    """
    try:
        # Get username from query params if provided
        username = request.query_params.get('username')
        
        # If username is provided, try to logout that specific user
        if username:
            try:
                user = User.objects.get(username=username)
                message = f"User {username} logged out successfully"
            except User.DoesNotExist:
                message = f"User {username} not found, but session cleared"
        else:
            message = "Logged out successfully"
        
        # Clear the current session
        django_logout(request)
        
        return Response({
            "success": True,
            "message": message,
            "username": username
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            "success": False,
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# cbv user model
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
