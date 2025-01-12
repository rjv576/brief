from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
import datetime

from .models import Debt, PaymentMethod
from .forms import DebtForm

# Create your views here.


def base(request):
    return render(request, 'debts/base.html')

def debt_list(request):
    debts = Debt.objects.all()
    return render(request, 'debts/debt_list.html', {'debts': debts})

def select_payment_method(request, debt_id):
    debt = get_object_or_404(Debt, id=debt_id)
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        # Verificamos si el método existe
        if payment_method in ['avalanche', 'snowball']:
            # Obtener el método de pago asociado
            selected_method = PaymentMethod.objects.create(
                debt=debt,
                method=payment_method,
                monthly_payment=debt.minimum_payment  # Aquí puedes ajustar el pago mensual
            )
            
            return redirect('calculate_payments', debt_id=debt.id)  # Redirige a la página de cálculo

    return render(request, 'debts/select_payment_method.html', {'debt': debt})
        
        
def add_debt(request):
    if request.method == 'POST':
       form = DebtForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('debt_list')
    else:
        form = DebtForm()
    return render(request, 'debts/add_debt.html', {'form': form})

def calculate_payments(request, debt_id):
    # Obtener la deuda por ID
    debt = get_object_or_404(Debt, id=debt_id)
    
    # Obtener los métodos de pago disponibles para esa deuda
    payment_methods = PaymentMethod.objects.filter(debt=debt)
    
    if request.method == "POST":
        # Obtener el método de pago seleccionado desde el formulario
        selected_method_id = request.POST.get("payment_method")
        
        if not selected_method_id:
            return HttpResponseBadRequest("No se seleccionó un método de pago.")
        
        # Obtener el método de pago seleccionado
        payment_method = get_object_or_404(PaymentMethod, id=selected_method_id)
        
        # Lógica para calcular la distribución de los pagos y la fecha de liquidación
        monthly_payment = float(payment_method.monthly_payment)
        months_to_pay = float(debt.total_amount / monthly_payment)
        total_paid = float(monthly_payment * months_to_pay)
        total_saved = float(total_paid - debt.total_amount)
        
        # Calcular la fecha de liquidación estimada
        due_date = datetime.date.today()
        due_date = due_date.replace(day=1)  # Empezamos desde el primer día del mes
        due_date = due_date.replace(month=due_date.month + int(months_to_pay))  # Aumentamos los meses necesarios

        # Renderizar los resultados de los cálculos
        return render(request, 'debts/payment_results.html', {
            'debt': debt,
            'payment_method': payment_method,
            'months_to_pay': int(months_to_pay),
            'total_paid': round(total_paid, 2),
            'total_saved': round(total_saved, 2),
            'due_date': due_date.strftime('%B %Y'),
        })
    
    # Si no se ha enviado el formulario (primera carga de la página), renderizamos la selección del método de pago
    return render(request, 'debts/calculate_payments.html', {
        'debt': debt,
        'payment_methods': payment_methods,
    })