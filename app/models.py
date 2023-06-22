from django.db import models

class ApiKey(models.Model):
    API_SERVICES_CHOICES = (
        ('Dowell Mail', 'Dowell Mail'),
        ('Dowell Scale', 'Dowell Scale'),
    )
    APIKey = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    api_services = models.CharField(max_length=255, choices=API_SERVICES_CHOICES, unique=True)
    is_active = models.BooleanField(default=True)
    credits = models.IntegerField(default=50, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    workspace_id = models.CharField(max_length=255,null=True)
    userDetails = models.JSONField(null=True, blank=False)

    def __str__(self):
        return str(self.APIKey)

class Voucher(models.Model):
    voucher_name = models.CharField(max_length=255,unique=True)
    voucher_code = models.CharField(max_length=255,unique=True)
    voucher_discount = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.voucher_name)
    
class RedeemVoucher(models.Model):
    email = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    voucher_code = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return str(self.name)