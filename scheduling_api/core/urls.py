from django.urls import path, include
from core.views import ScheduleCallView, ServerStateView 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('main', ScheduleCallView, basename='main-view')


urlpatterns = [
    path('', include(router.urls)),
    path('ping/', ServerStateView.as_view(), name='ping-test')
]


