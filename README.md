# Calendario con Tareas Pendientes

Este proyecto es un **prototipo** de aplicación de calendario desarrollado en Python, utilizando la biblioteca `tkinter` para la interfaz gráfica. Permite al usuario visualizar un calendario, agregar notas asociadas a fechas específicas y mostrar las tareas pendientes.

## Funcionalidades implementadas

1. **Visualización del calendario**: 
   - Muestra un calendario mensual interactivo.
   - Distingue los días pasados de los futuros con colores y estados de los botones.
   - Navegación entre meses y años.

2. **Gestión de notas**:
   - Permite agregar tareas con fecha y hora específicas.
   - Guarda las notas en un archivo de texto llamado `notas.txt`.
   - Muestra las tareas pendientes ordenadas por fecha, indicando cuántos días faltan.

3. **Interfaz gráfica**:
   - Ventanas emergentes para ingresar notas y seleccionar fechas.
   - Uso de widgets como `Combobox`, `Text`, y `Button` de `tkinter`.

## Requisitos

- Python 3.6 o superior.
- Configuración regional en español para mostrar nombres de días y meses correctamente (`es_ES.UTF-8`).
- Un archivo llamado `notas.txt` en el mismo directorio donde se ejecuta el script (se creará solo si no existe), para guardar las tareas.

## Instalación y ejecución

1. Clona este repositorio o descarga el archivo del script.
2. Asegúrate de tener configurado el entorno local en español (`locale es_ES.UTF-8`).
3. Ejecuta el script principal:

   ```bash
   python calendario.py
