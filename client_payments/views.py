from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Payment
from django.db.models import Max




class PaymentListView(ListView):
    model = Payment
    template_name = 'client_payments/payment.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'payments'
    ordering = ['-date_posted']
    paginate_by = 12





class UserPaymentListView(ListView):
    model = Payment
    template_name = 'client_payments/user_payments.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'payments'
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Payment.objects.filter(user=user).order_by('-date_posted')


class PaymentDetailView(DetailView):
    model = Payment


class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class PaymentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Payment
    fields = ['title', 'amount_paid']

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

    def test_func(self):
        payment = self.get_object()
        if self.request.user == payment.client:
            return True
        return False


class PaymentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Payment
    success_url = '/'

    def test_func(self):
        payment = self.get_object()
        if self.request.user == payment.client:
            return True
        return False