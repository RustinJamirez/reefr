from django.contrib import admin

from reefr_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.Tank)
admin.site.register(models.ParameterType)