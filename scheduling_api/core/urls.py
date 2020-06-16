from django.urls import path, include
from core.views import ScheduleCallView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('main', ScheduleCallView, basename='main-view')


urlpatterns = [
    path('', include(router.urls)),
]


