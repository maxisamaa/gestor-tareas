from django.urls import path
from . import views

from django.urls import path
from tareas.views import ListaTareasView, AgregarTareaView, DetalleTareaView, EliminarTareaView

urlpatterns = [
    path('', ListaTareasView.as_view(), name='lista_tareas'),
    path('agregar/', AgregarTareaView.as_view(), name='agregar_tarea'),
    path('<int:tarea_id>/', DetalleTareaView.as_view(), name='detalle_tarea'),
    path('<int:tarea_id>/eliminar/', EliminarTareaView.as_view(), name='eliminar_tarea'),
]
