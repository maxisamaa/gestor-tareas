# views_combined.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from tareas.forms import TareaForm
from tareas.memoria import TAREAS
# la lista tareas basada en un dic la cree en memoria.py
#metodos estaticos
def obtener_tareas_usuario(user):
    if user.id not in TAREAS:
        TAREAS[user.id] = []
    return TAREAS[user.id]

def siguiente_id(tareas):
    if not tareas:
        return 1
    return max(t['id'] for t in tareas) + 1
#metodos de clases
class ListaTareasView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')  # usa el nombre de la url de login
    def get(self, request):
        tareas = obtener_tareas_usuario(request.user)
        return render(request, 'lista.html', {'tareas': tareas})

class DetalleTareaView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request, tarea_id):
        tareas = obtener_tareas_usuario(request.user)
        tarea = next((t for t in tareas if t['id'] == tarea_id), None)
        if not tarea:
            return redirect('lista_tareas')
        return render(request, 'detalle.html', {'tarea': tarea})

class AgregarTareaView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        form = TareaForm()
        return render(request, 'agregar.html', {'form': form})

    def post(self, request):
        form = TareaForm(request.POST)
        if form.is_valid():
            tareas = obtener_tareas_usuario(request.user)
            nueva = {
                'id': siguiente_id(tareas),
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion']
            }
            tareas.append(nueva)
            return redirect('lista_tareas')
        return render(request, 'agregar.html', {'form': form})

class EliminarTareaView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request, tarea_id):
        tareas = obtener_tareas_usuario(request.user)
        tarea = next((t for t in tareas if t['id'] == tarea_id), None)
        return render(request, 'eliminar.html', {'tarea': tarea})

    def post(self, request, tarea_id):
        tareas = obtener_tareas_usuario(request.user)
        tareas[:] = [t for t in tareas if t['id'] != tarea_id]
        return redirect('lista_tareas')