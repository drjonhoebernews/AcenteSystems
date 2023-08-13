from django.urls import path
from . import views

urlpatterns = [
    path('list', views.FAQListView.as_view(), name='faq-list'),
    path('detail/<int:pk>', views.FAQDetailView.as_view(), name='faq-detail'),
]
