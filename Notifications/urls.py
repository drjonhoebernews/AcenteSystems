from django.urls import path
from . import views

urlpatterns = [
    path('list', views.NotificationListView.as_view(), name='notification-list'),
    path('detail/<int:pk>', views.NotificationDetailView.as_view(), name='notification-detail'),
]
