from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Plot(models.Model):
    plot_number = models.CharField(max_length=100)

    def __str__(self):
        return self.plot_number

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    plot = models.ForeignKey(Plot,  on_delete= models.CASCADE,  blank=True, null=True, help_text='optional')
    buying_price = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    total_amount_paid = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    reciept_number =  models.CharField(null=True, blank=True, max_length=200, unique=True)
    is_published = models.BooleanField(default=True)
    reciept_date = models.DateTimeField(default=timezone.now)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return  f' {self.user.username}--- Plot number {self.plot} ---payment date {self.reciept_date}'

    def get_absolute_url(self):
        return reverse('payment-detail', kwargs={'pk': self.pk})
