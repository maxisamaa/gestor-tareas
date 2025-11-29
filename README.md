# 📝 Gestor de Tareas – Proyecto Django

Este proyecto es un Gestor de Tareas desarrollado con Django, que permite a los usuarios registrarse, iniciar sesión y gestionar sus propias tareas de forma privada. Cada usuario puede crear, ver y eliminar tareas, además de visualizar un detalle individual de cada una. El sistema está estructurado siguiendo el patrón MVT de Django ( sin base de datos para los modelos ), e incluye autenticación, manejo de sesiones, plantillas reutilizables y una organización clara del proyecto.

## 📂 Estructura del Proyecto

El proyecto está organizado en los siguientes componentes principales:

### Proyecto Django (`gestor_tareas/`)

Contiene la configuración general del sistema, como `settings.py`, `urls.py` y archivos de inicialización.

### Aplicación principal (`tareas/`)

Incluye vistas, modelos, URLs, lógica de negocio y plantillas relacionadas con:

- Gestión de tareas  
- Listado de tareas  
- Detalle de cada tarea  
- Creación y eliminación  

### Sistema de Usuarios

Basado en el modelo `User` de Django, permitiendo registro, login y logout.  

### Plantillas (`templates/`)

Contiene `base.html` y las vistas extendidas para mostrar la información al usuario.

## ⚙️ Funcionalidades Principales

- Registro e inicio de sesión de usuarios.  
- Creación de un perfil asociado a cada usuario.  
- Listado de tareas propias del usuario.  
- Vista detallada de cada tarea.  
- Eliminación de tareas.  
- Interfaz basada en plantillas HTML extendidas desde `base.html`.  
- Acceso protegido mediante `LoginRequiredMixin`.

## ▶️ Ejecución del Proyecto

Puedes acceder a la aplicación directamente desde la siguiente URL: ( ficticio , es el host puesto en allowed host , ademas esta puesto en DEBUG FALSE)

**<https://gestor-tareas.cl/>** 
