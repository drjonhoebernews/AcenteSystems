from django.urls import path
from . import views

urlpatterns = [
    path('list', views.TowTruckListView.as_view(), name='towtruck-list'),
    path('detail/<int:pk>', views.TowTruckDetailView.as_view(), name='towtruck-detail'),
]
