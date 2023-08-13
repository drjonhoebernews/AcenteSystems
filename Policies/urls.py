from django.urls import path
from . import views

urlpatterns = [
    path('list', views.PolicyListView.as_view(), name='policy-list'),
    path('detail/<int:pk>', views.PolicyDetailView.as_view(), name='policy-detail'),
]
