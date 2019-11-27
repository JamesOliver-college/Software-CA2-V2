from django.urls import path
from . import views

app_name = 'vouchers'

url_patterns = [
    path('apply/', views.voucher_apply, name='apply'),
]