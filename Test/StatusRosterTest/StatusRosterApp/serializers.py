from rest_framework import serializers
from django.contrib.auth.hashers import make_password 
from .models import Cluster, Member, Roster, Status

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = '__all__'

class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roster
        fields = '__all__'

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'