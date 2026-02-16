from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Subscription, Card, Address, Bill,
    Customer, Lead, Project
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        source='customer',
        write_only=True
    )

    class Meta:
        model = Card
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    # Nested customer and address read-only
    customer = serializers.StringRelatedField(read_only=True)
    address = serializers.StringRelatedField(read_only=True)
    
    # Write-only fields for POST/PUT
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        source='customer',
        write_only=True
    )
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        source='address',
        write_only=True
    )

    class Meta:
        model = Bill
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(read_only=True)
    subscription_id = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.all(),
        source='subscription',
        write_only=True
    )

    # Reverse FK fetching using 'source'
    cards = CardSerializer(source='customer_card', many=True, read_only=True)
    bills = BillSerializer(source='customer_bill', many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'




class LeadSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField(read_only=True)

    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='assigned_to',
        write_only=True
    )

    address = AddressSerializer(read_only=True)
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        source='address',
        write_only=True
    )

    class Meta:
        model = Lead
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(read_only=True)
    subscription_id = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.all(),
        source='subscription',
        write_only=True
    )

    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        source='customer',
        write_only=True
    )

    assignedTo = serializers.StringRelatedField(read_only=True)
    assignedTo_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='assignedTo',
        write_only=True
    )

    class Meta:
        model = Project
        fields = '__all__'
