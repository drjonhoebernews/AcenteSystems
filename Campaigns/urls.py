from django.urls import path
from . import views

urlpatterns = [
    path('list', views.CampaignListView.as_view(), name='campaign-list'),
    path('detail/<int:pk>', views.CampaignDetailView.as_view(), name='campaign-detail'),
]
