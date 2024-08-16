# funciones.py

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv
import os

# Cargar el archivo .env
load_dotenv()

# Alcances que se van a utilizar
ALCANCES = ['https://www.googleapis.com/auth/drive']

def cargar_credenciales():
    """Carga o genera las credenciales necesarias."""
    credenciales = None
    try:
        if os.path.exists('token.json'):
            credenciales = Credentials.from_authorized_user_file('token.json', ALCANCES)
        if not credenciales or not credenciales.valid:
            if credenciales and credenciales.expired and credenciales.refresh_token:
                credenciales.refresh(Request())
            else:
                flujo = InstalledAppFlow.from_client_secrets_file('credentials.json', ALCANCES)
                credenciales = flujo.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(credenciales.to_json())
    except Exception as e:
        print(f"Error al cargar o generar las credenciales: {e}")
        raise
    return credenciales

def conectar_api():
    """Conecta a la API de Google Drive y retorna el servicio."""
    try:
        credenciales = cargar_credenciales()
        servicio = build('drive', 'v3', credentials=credenciales)
        return servicio
    except Exception as e:
        print(f"Error al conectar a la API de Google Drive: {e}")
        raise

def obtener_id_carpeta(servicio, nombre_carpeta):
    """Busca una carpeta por nombre y retorna su ID."""
    try:
        consulta = f"mimeType='application/vnd.google-apps.folder' and name='{nombre_carpeta}' and trashed=false"
        respuesta = servicio.files().list(q=consulta, fields="files(id, name)").execute()
        carpetas = respuesta.get('files', [])
        if carpetas:
            return carpetas[0]['id']
        return None
    except Exception as e:
        print(f"Error al obtener el ID de la carpeta: {e}")
        raise

def crear_carpeta(servicio, nombre_carpeta):
    """Crea una nueva carpeta y retorna su ID."""
    try:
        metadatos_archivo = {
            'name': nombre_carpeta,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        carpeta = servicio.files().create(body=metadatos_archivo, fields='id').execute()
        return carpeta.get('id')
    except Exception as e:
        print(f"Error al crear la carpeta: {e}")
        raise

def subir_archivo(servicio, directorio, id_carpeta):
    """Sube archivos desde un directorio a Google Drive en la carpeta especificada."""
    try:
        for archivo_nombre in os.listdir(directorio):
            archivo_ruta = os.path.join(directorio, archivo_nombre)
            if os.path.isfile(archivo_ruta):
                metadatos_archivo = {
                    'name': archivo_nombre,
                    'parents': [id_carpeta]
                }
                media = MediaFileUpload(archivo_ruta, resumable=True)
                archivo_subido = servicio.files().create(body=metadatos_archivo, media_body=media, fields='id').execute()
                print(f"Archivo '{archivo_nombre}' subido con ID: {archivo_subido.get('id')}")
    except Exception as e:
        print(f"Error al subir los archivos: {e}")
        raise
