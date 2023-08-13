from django.urls import path
from . import views

urlpatterns = [
    path('list', views.ReviewListView.as_view(), name='review-list'),
    path('detail/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
]
