from django.contrib import admin

from apis.transactionotps.models import TransactionOtp


@admin.register(TransactionOtp)
class AdminAuthOtp(admin.ModelAdmin):
    list_display = ('transaction', 'otp', 'expiry', 'description', 'date_created', 'date_updated')
