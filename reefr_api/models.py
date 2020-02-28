from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.core.validators import MinValueValidator

import datetime


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User email not specified')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """"Database model for users in system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """"Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text


class Tank(models.Model):
    """A fish tank model"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=255)
    created_on = models.DateField(default=datetime.date.today, blank=False)
    volume = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )
    volume_units = models.CharField(choices=[('GAL', 'gallons'), ('LTR', 'liters')], max_length=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        """Return the model as a string"""
        return self.name


class UserParameterType(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=32)
    unit = models.CharField(max_length=32)
    min_safe = models.FloatField()
    max_safe = models.FloatField()

    def __str__(self):
        """Return the model as a string"""
        return self.name


class ParameterType(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=32)
    unit = models.CharField(max_length=32, blank=True)
    min_safe = models.FloatField()
    max_safe = models.FloatField()
    default = models.BooleanField(default=False)

    def __str__(self):
        """Return the model as a string"""
        return self.name


class ParameterMeasurement(models.Model):
    """Tank measurement"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )
    tank_id = models.ForeignKey(
        'Tank',
        on_delete=models.DO_NOTHING
    )
    parameter = models.ForeignKey(
        'ParameterType',
        on_delete=models.DO_NOTHING
    )
    value = models.FloatField()
    measured_on = models.DateTimeField(default=datetime.datetime.now)
    notes = models.CharField(max_length=255)

    def __str__(self):
        """Return the model as a string"""
        return f'{self.parameter.name} {self.value}'


class Fish(models.Model):
    """A Fish"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )
    tank_id = models.ForeignKey(
        'Tank',
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    added_on = models.DateField(default=datetime.date.today)


class Equipment(models.Model):
    """Tank equipment"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )
    tank_id = models.ForeignKey(
        'Tank',
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    added_on = models.DateField(default=datetime.date.today)


class Image(models.Model):
    """Images of tank, fish, equipment, etc"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )
    tank_id = models.ForeignKey(
        'Tank',
        on_delete=models.DO_NOTHING
    )
    description = models.CharField(max_length=255)
    file = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.file.name

