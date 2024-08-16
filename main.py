# main.py

from funciones import conectar_api, obtener_id_carpeta, crear_carpeta, subir_archivo
import os

def main():
    """Función principal para buscar o crear la carpeta y subir los archivos."""
    try:
        servicio = conectar_api()
        nombre_carpeta = os.getenv('NOMBRE_CARPETA')
        directorio = os.getenv('DIRECTORIO')

        if not nombre_carpeta or not directorio:
            raise ValueError("Las variables de entorno 'NOMBRE_CARPETA' y 'DIRECTORIO' deben estar definidas.")

        id_carpeta = obtener_id_carpeta(servicio, nombre_carpeta)
        if not id_carpeta:
            id_carpeta = crear_carpeta(servicio, nombre_carpeta)

        subir_archivo(servicio, directorio, id_carpeta)

    except Exception as e:
        print(f"Error en la ejecución del script: {e}")

if __name__ == '__main__':
    main()
