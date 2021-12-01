from django.urls import path
from . import views
#el punto antes del import, quiere decir que busque todo de esta misma carpeta

app_name = 'productos'

urlpatterns = [

    path('listar/', views.ListarProductos, name = 'listar_productos')
   
]

