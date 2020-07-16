from django.urls import path
from core.views import home, login, registro, reserva, nosotros, nueva_reserva, productos_form, productos_list

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('reserva/', reserva, name="reserva"),
    path('nosotros/', nosotros, name="nosotros"),
    path('nueva_reserva/', nueva_reserva, name="nueva_reserva"),
    path('productos_form/', productos_form, name="productos_form"),
    path('productos_list/', productos_list, name="productos_list"),
]