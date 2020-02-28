from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from reefr_api import serializers
from reefr_api import models
from reefr_api import permissions

from itertools import chain


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,  )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating profile feed items"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets user profile to logged in user"""
        serializer.save(user_profile=self.request.user)


class TankViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating profile feed items"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.TankSerializer
    # queryset = models.Tank.objects.filter(user=self.request.user)
    permission_classes = (
        permissions.ShowOwnTank,
        IsAuthenticated
    )

    def get_queryset(self):
        return models.Tank.objects.filter(user_profile=self.request.user)

    def perform_create(self, serializer):
        """Sets user profile to logged in user"""
        serializer.save(user_profile=self.request.user)


class ParameterTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ParameterTypeSerializer
    permission_classes = (
        permissions.UpdateOwnUserParameters,
        IsAuthenticated,
    )

    def get_queryset(self):
        user_param_queryset = models.ParameterType.objects.filter(user_profile=self.request.user)
        param_queryset = models.ParameterType.objects.filter(default=True)
        return list(chain(param_queryset, user_param_queryset))

    def perform_create(self, serializer):
        """Sets user profile to logged in user"""
        serializer.save(user_profile=self.request.user, default=False)


class ParameterMeasurementViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ParameterMeasurementSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return models.ParameterMeasurement.objects.filter(
            user_profile=self.request.user
        )

    def perform_create(self, serializer):
        """Sets user profile to logged in user"""
        serializer.save(user_profile=self.request.user)


class FishViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.FishSerializer
    permission_classes = (
        permissions.UpdateAndViewOwnFish,
        IsAuthenticated
    )

    def get_queryset(self):
        return models.Fish.objects.filter(
            user_profile=self.request.user
        )

    def perform_create(self, serializer):
        """Sets user profile to logged in user"""
        serializer.save(user_profile=self.request.user)


class EquipmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.EquipmentSerializer
    permission_classes = (
        permissions.UpdateAndViewOwnEquipment,
        IsAuthenticated
    )

    def get_queryset(self):
        return models.Equipment.objects.filter(
            user_profile=self.request.user
        )

    def perform_create(self, serializer):
        """Sets user profile to logged in user"""
        serializer.save(user_profile=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ImageSerializer
    permission_classes = (
        permissions.UpdateAndViewOwnImage,
        IsAuthenticated
    )

    def get_queryset(self):
        return models.Equipment.objects.filter(
            user_profile=self.request.user
        )

    def perform_create(self, serializer):
        """Sets user profile to logged in user"""
        serializer.save(user_profile=self.request.user)
