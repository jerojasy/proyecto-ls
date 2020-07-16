from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
from .models import Reserva, Producto
from .forms import ReservaForm, ProductosForm


# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def registro(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            #autentificar y redirigir al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
        else : 
            data["message"] = "No se pudo completar el registro, favor valide que sus datos sean correctos e intentelo de nuevamente."

    return render(request, 'registration/registro.html', data)

@login_required
def reserva(request):
    reservas = Reserva.objects.all()
    data = {
        'misreservas':reservas
    }
   
    return render(request, 'core/reserva.html', data)

def nosotros(request):
    return render(request, 'core/nosotros.html')

@login_required
def nueva_reserva(request):
    data = {
        'form':ReservaForm()
    }

    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Agendado Correctamente."

    return render(request, 'core/nueva_reserva.html', data)


def productos_list(request):
    context = {'productos_list' : Producto.objects.all()}
    return render(request , 'core/productos_list.html')
    

def productos_form(request):
    if request.method=='GET':
        form = ProductosForm()
        return render(request , 'core/productos_form.html', {'form':form}) 
    else: 
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'core/productos_list.html')


def productos_eliminar(request):
    return