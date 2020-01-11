from django.contrib import admin
from .models import Payment, Plot


admin.site.register(Plot)


class PaymentAdmin(admin.ModelAdmin):
  list_display = ( 'user', 'plot', 'buying_price', 'amount_paid', 'reciept_number','total_amount_paid',  'current_balance',  'reciept_date', 'date_posted', 'is_published',)
  list_display_links = ('user', 'plot')
  list_filter = ('user','plot')
  list_editable = ('is_published',)
  search_fields = ('user',  'plot', 'receipt_number')
  list_per_page = 25

admin.site.register(Payment, PaymentAdmin)

