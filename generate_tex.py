import os

# Lista de secciones
sections = [
    "Introducción",
    "ZMROBO",
    "RoboSim",
    "Características",
    "Instalación de la plataforma",
    "Interfaz de usuario",
    "Opciones disponibles",
    "Ventajas y desventajas",
    "Aplicación",
    "Costos",
    "Comparación de RoboSim y RoboDK",
    "Conclusiones",
    "Referencias"
]

# Ruta donde quieres guardar los archivos .tex
ruta = r"C:\Users\Elbin\Documents\Universidad\Semestre II\Ing. Sistemas Robóticos\Parciales\Parcial #3"

# Verificar que la ruta existe
if not os.path.exists(ruta):
    print("La ruta especificada no existe.")
else:
    # Crear un archivo .tex para cada sección en la ruta especificada
    for section in sections:
        # Nombre del archivo será el nombre de la sección, en minúsculas y con espacios reemplazados por guiones
        file_name = section.lower().replace(" ", "_") + ".tex"
        
        # Ruta completa del archivo
        file_path = os.path.join(ruta, file_name)
        
        # Contenido para cada archivo .tex (solo el nombre de la sección)
        tex_content = f"\\section{{{section}}}\n"
        
        # Escribir el contenido en un archivo .tex
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(tex_content)
        
        print(f"Archivo '{file_name}' ha sido creado en la ruta {file_path}.")
