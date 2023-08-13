from django.urls import path
from . import views

urlpatterns = [
    path('list', views.VehicleListView.as_view(), name='vehicle-list'),
    path('detail/<int:pk>', views.VehicleDetailView.as_view(), name='vehicle-detail'),
]
