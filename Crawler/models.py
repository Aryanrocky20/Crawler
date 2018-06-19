# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class CryptoCurrency(models.Model):
    CryptoCode = models.CharField(max_length=10)
    CryptoName = models.CharField(max_length=20)

    def __str__(self):
        return self.CryptoCode

class CurrencyChanges(models.Model):
    CryptoCode = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    curPrice = models.FloatField(max_length=10)
    prevPrice = models.FloatField(max_length=10)
    inBTC = models.FloatField(max_length=10)
