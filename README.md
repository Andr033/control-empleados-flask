# Sistema de Control de Empleados

Aplicación web desarrollada con **Flask** para gestionar empleados, consultar información de nóminas y visualizar estadísticas mediante gráficos interactivos.

El sistema permite:

- Registrar y gestionar empleados.
- Consultar datos de nóminas.
- Mostrar estadísticas mediante gráficos.
- Calcular el gasto total en diferentes divisas usando conversión de moneda en tiempo real.

## Requisitos

Antes de instalar el proyecto, asegúrate de tener instalado:

- Python 3.8 o superior
- Git (opcional, solo si vas a clonar el repositorio)

## Instalación

### 1. Descargar el proyecto

Puedes clonar el repositorio usando Git:

```bash
git clone https://github.com/Andr033/control-empleados-flask.git
cd <NOMBRE_DE_LA_CARPETA>
```
Si tienes el proyecto en un archivo ZIP, simplemente extráelo y abre una terminal dentro de la carpeta del proyecto.

### 2. Crear un entorno virtual

Es recomendable utilizar un entorno virtual para mantener las dependencias separadas del resto de proyectos.

Windows
```bash
python -m venv venv
venv\Scripts\activate
```
macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

Con el entorno virtual activo, instala las librerías necesarias:

pip install -r requirements.txt

Esto instalará automáticamente las dependencias utilizadas por el proyecto, como:

- Flask
- Flask-SQLAlchemy
- pandas
- matplotlib
- requests

Ejecutar la aplicación
# 1. Iniciar el servidor

Ejecuta el archivo principal:

python app.py

Si todo funciona correctamente, Flask iniciará el servidor local.

# 2. Abrir la aplicación

Accede desde tu navegador a:

http://127.0.0.1:5000
Estructura del proyecto
.
├── app.py
├── empleados.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── nuevo.html
Archivos principales

app.py
Contiene la configuración principal de Flask, las rutas de la aplicación, la lógica de gestión de empleados, cálculos de nómina y generación de gráficos.

empleados.py
Define el modelo de datos de empleados utilizando SQLAlchemy con una base de datos SQLite.

templates/
Carpeta donde se encuentran las páginas HTML utilizadas por la aplicación.

requirements.txt
Lista de dependencias necesarias para ejecutar el proyecto.

Tecnologías utilizadas
Python
Flask
Flask-SQLAlchemy
SQLite
HTML / CSS
pandas
matplotlib
Notas

Este proyecto está pensado para ejecutarse en local y puede ampliarse añadiendo autenticación, más estadísticas o conexión con otros sistemas de gestión.
