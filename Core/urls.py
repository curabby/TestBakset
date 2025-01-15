from django.urls import path
from .views import VPSListCreateAPIView, VPSListAPIView, CurrentVPSAPIView, StatusVPSUpdateAPIView


urlpatterns = [
    path('create/', VPSListCreateAPIView.as_view(), name='create_new_vps'),
    path('getvps/', VPSListAPIView.as_view(), name='get_vps'),
    path('getvps/<str:uid>', CurrentVPSAPIView.as_view(), name='get_current_vps'),
    path('status-update/<str:uid>', StatusVPSUpdateAPIView.as_view(), name='create_new_vps'),
]