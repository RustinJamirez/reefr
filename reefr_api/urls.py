from django.urls import path, include

from rest_framework.routers import DefaultRouter

from reefr_api import views

router = DefaultRouter()
router.register('tank', views.TankViewSet, base_name="tank")
router.register('profile', views.UserProfileViewSet)
router.register('parameters', views.ParameterTypeViewSet, base_name="parameters")
router.register('measure', views.ParameterMeasurementViewSet, base_name="measure")
# router.register('fish', views.FishViewSet, base_name="fish")
# router.register('equipment', views.EquipmentViewSet, base_name='equipment')
# router.register('image', views.ImageViewSet, base_name='image')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

