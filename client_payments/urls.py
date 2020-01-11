from django.urls import path
from .views import (
    PaymentListView,
    PaymentDetailView,
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
    UserPaymentListView
)
from . import views

urlpatterns = [
    path('', PaymentListView.as_view(), name='payments'),
    path('user/<str:username>', UserPaymentListView.as_view(), name='user-payments'),
    path('payment/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('Payment/new/', PaymentCreateView.as_view(), name='payment-create'),
    path('payment/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment-update'),
    path('payment/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment-delete'),

]