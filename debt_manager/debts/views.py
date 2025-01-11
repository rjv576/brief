from django.shortcuts import render
from .models import Debt, PaymentMethod
# Create your views here.
def base(request):
    return render(request, 'debts/base.html')

def debt_list(request):
    debts = Debt.objects.all()
    return render(request, 'debts/debt_list.html', {'debts': debts})

def payment_method_list(request):
    payment_methods = PaymentMethod.objects.all()
    return render(request, 'debts/payment_method_list.html', {'payment_methods': payment_methods})

def calculate_payments(request, debt_id):
    debt = Debt.objects.get(id=debt_id)
    payment_methods = PaymentMethod.objects.filter(debt=debt)
    
    # Logica para calcular la distribucion de los pagos y pechas 
    # Supniendo que solo se tiene un metododo de pago poor deuda
    if payment_methods.exists():
        payment_method = payment_methods.first()
        # Calculamos la cantidad de meses necesarios para pagar la deuda
        months_to_pay = debt.balance / payment_method.monthly_payment
        total_paid = payment_method.monthly_payment * months_to_pay
        total_saved = total_paid - debt.balance
    else:
        months_to_pay = 0
        total_paid = 0
        total_saved = 0
        
        return render(request, 'debts/calculate_payments.html', {
            'debt': debt,
            'payment_method': payment_method,
            'months_to_pay': months_to_pay,
            'total_paid': total_paid,
            'total_saved': total_saved
        })