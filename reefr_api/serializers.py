from rest_framework import serializers

from reefr_api import models

from itertools import chain


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed item"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }


class TankSerializer(serializers.ModelSerializer):
    """Serializes profile feed item"""

    class Meta:
        model = models.Tank
        fields = ('id', 'user_profile', 'name', 'created_on', 'volume', 'volume_units', 'description')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }


class UserParameterTypeSerializer(serializers.ModelSerializer):
    """Serializes Parameter Type"""
    class Meta:
        model = models.UserParameterType
        fields = ('id', 'user_profile', 'name', 'unit', 'max_safe', 'min_safe')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }


class ParameterTypeSerializer(serializers.ModelSerializer):
    """Serializes Parameter Type"""
    class Meta:
        model = models.ParameterType
        fields = ('id', 'name', 'unit', 'max_safe', 'min_safe')
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'unit': {'read_only': True},
            'max_safe': {'read_only': True},
            'min_safe': {'read_only': True}
        }


class UserTankForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return models.Tank.objects.filter(user_profile=self.context['request'].user)


class UserParameters(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user_param_queryset = models.UserParameterType.objects.filter(
            user_profile=self.context['request'].user
        )
        param_queryset = models.ParameterType.objects.all()
        return list(chain(param_queryset, user_param_queryset))


class ParameterMeasurementSerializer(serializers.ModelSerializer):
    """Serializes profile feed item"""
    tank_id = UserTankForeignKey()
    parameter = UserParameters()

    class Meta:
        model = models.ParameterMeasurement
        fields = ('id', 'tank_id', 'parameter', 'value', 'measured_on', 'notes',)

