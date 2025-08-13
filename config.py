import os

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_RESOLUCIONES = os.path.join(BASE_DIR, 'resoluciones_pdf')
CARPETA_PROCESADOS = os.path.join(BASE_DIR, 'procesados')
CARPETA_LOGS = os.path.join(BASE_DIR, 'logs')
CARPETA_TEMP = os.path.join(BASE_DIR, 'temp')

# Configuración del servidor SMTP
SMTP_CONFIG = {
    'server': 'smtp.gmail.com',
    'port': 587,
    'username': 'jhniconstain@unicauca.edu.co',
    'password': 'yemo fooy ubhe mvwh',
    'from_email': 'jhniconstain@unicauca.edu.co',
    'subject_prefix': 'COMUNICACIÓN RESOLUCION {numero} DEL 2025'
}

# Crear carpetas si no existen
os.makedirs(CARPETA_RESOLUCIONES, exist_ok=True)
os.makedirs(CARPETA_PROCESADOS, exist_ok=True)
os.makedirs(CARPETA_LOGS, exist_ok=True)
os.makedirs(CARPETA_TEMP, exist_ok=True)