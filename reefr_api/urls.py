from django.urls import path, include

from rest_framework.routers import DefaultRouter

from reefr_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('tank', views.TankViewSet, base_name="tank")
router.register('profile', views.UserProfileViewSet)
router.register('parameters', views.ParameterTypeViewSet, base_name="parameters")
router.register('user-parameter', views.UserParameterTypeViewSet, base_name="user-parameters")
router.register('measure', views.ParameterMeasurementViewSet, base_name="measure")
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]