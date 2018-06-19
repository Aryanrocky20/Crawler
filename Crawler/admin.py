# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CryptoCurrency, CurrencyChanges

# Register your models here.

admin.site.register(CryptoCurrency),
admin.site.register(CurrencyChanges)
