from django.urls import path, include
from rest_framework.routers import DefaultRouter
from StatusRosterApp.views import ClusterViewSet, MemberViewSet, LoginAPI, RosterViewSet, ResetPasswordView, StatusViewSet

router = DefaultRouter()
router.register(r'cluster', ClusterViewSet, basename='cluster')
router.register(r'register', MemberViewSet, basename='register')
router.register(r'roster', RosterViewSet, basename='roster')
router.register(r'status', StatusViewSet, basename='status')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPI.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]
