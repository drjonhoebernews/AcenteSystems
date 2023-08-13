from django.urls import path
from . import views

urlpatterns = [
    path('list', views.UserListView.as_view(), name='user-list'),
    path('detail/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]
