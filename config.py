import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_RESOLUCIONES = os.path.join(BASE_DIR, 'resoluciones_pdf')
CARPETA_PROCESADOS = os.path.join(BASE_DIR, 'procesados')
CARPETA_LOGS = os.path.join(BASE_DIR, 'logs')
CARPETA_TEMP = os.path.join(BASE_DIR, 'temp')

# Configuración del servidor SMTP desde variables de entorno
SMTP_CONFIG = {
    'server': os.getenv('SMTP_SERVER'),
    'port': int(os.getenv('SMTP_PORT', 587)),
    'username': os.getenv('SMTP_USERNAME'),
    'password': os.getenv('SMTP_PASSWORD'),
    'from_email': os.getenv('SMTP_FROM_EMAIL'),
    'subject_prefix': os.getenv('SMTP_SUBJECT_PREFIX', 'COMUNICACIÓN RESOLUCION {numero} DEL 2025')
}

# Crear carpetas si no existen
os.makedirs(CARPETA_RESOLUCIONES, exist_ok=True)
os.makedirs(CARPETA_PROCESADOS, exist_ok=True)
os.makedirs(CARPETA_LOGS, exist_ok=True)
os.makedirs(CARPETA_TEMP, exist_ok=True)