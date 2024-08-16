# Script de Subida Automática de Fotos a Google Drive

Este script fue creado para automatizar la subida de fotos desde un directorio local a Google Drive. Lo desarrollé porque, después de haber tomado cientos de fotos con mi cámara, no quería subirlas manualmente a Google Drive.

## Requisitos

Antes de empezar, asegúrate de tener lo siguiente:

1. **Python 3.x** instalado en tu sistema.
2. Las dependencias listadas en `requirements.txt` instaladas.
3. Una cuenta de Google con acceso a Google Drive.
4. Acceso al servicio de API de Google Drive a través de Google Cloud.

## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu-usuario/nombre-del-repositorio.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd nombre-del-repositorio
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables de entorno:
    ```plaintext
    DIRECTORIO=/ruta/al/directorio/de/fotos
    CARPETA=NombreDeLaCarpetaEnDrive
    ```

    - **DIRECTORIO**: Ruta al directorio local donde se encuentran las fotos que deseas subir.
    - **CARPETA**: Nombre de la carpeta que se creará en Google Drive y donde se almacenarán las fotos.

5. Configura la API de Google Drive:

    - Ve a [Google Cloud Console](https://console.cloud.google.com/).
    - Crea un nuevo proyecto si no tienes uno.
    - Habilita la API de Google Drive para tu proyecto.
    - Crea credenciales OAuth 2.0 para una aplicación de escritorio.
    - Descarga el archivo `client_secrets.json` y renómbralo a `credentials.json`.
    - Coloca `credentials.json` en el directorio raíz del proyecto.

## Uso

Con todos los pasos anteriores completados, ya estás listo para usar el script. Simplemente ejecuta el siguiente comando:

```bash
python main.py
