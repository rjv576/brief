from django.db import models

# Create your models here.
class Debt(models.Model):
    name = models.CharField(max_length=100)
    total_amount = models.FloatField()
    interest_rate = models.FloatField()
    minimum_payment = models.FloatField()
    due_date = models.DateField()
    
    def __str__(self):
        return self.name
    
class PaymentMethod(models.Model):
    METHOD_CHOICES = [
        ('avalanche', 'Avalancha'),
        ('snowball', 'Bola de nieve'),
    ]
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)  # Método elegido
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, related_name="payment_methods")  # Relación con las deudas
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)  # Pago mensual total

    def __str__(self):
        return f"{self.method} - {self.debt.name}"