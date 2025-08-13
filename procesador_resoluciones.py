import os
import re
import shutil
from datetime import datetime
import pytesseract
from pdf2image import convert_from_path
from config import CARPETA_RESOLUCIONES, CARPETA_PROCESADOS, CARPETA_LOGS, CARPETA_TEMP
from enviar_correo import enviar_correo_resolucion
import cv2
import numpy as np

POPPLER_PATH = r"C:\poppler-24.08.0\Library\bin"

# Configurar ruta a Tesseract (Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocesar_imagen(imagen):
    """Mejora la imagen para OCR"""
    # Convertir a escala de grises
    gris = cv2.cvtColor(np.array(imagen), cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbral adaptativo
    procesada = cv2.adaptiveThreshold(
        gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 85, 11
    )
    
    return procesada

def extraer_texto_pdf(ruta_pdf):
    """Extrae texto de un PDF escaneado usando OCR"""
    texto_completo = ""
    
    # Convertir PDF a imágenes
    imagenes = convert_from_path(
        ruta_pdf,
        dpi=300,
        output_folder=CARPETA_TEMP,
        poppler_path=POPPLER_PATH
    )
    
    for i, imagen in enumerate(imagenes):
        # Preprocesar imagen
        imagen_procesada = preprocesar_imagen(imagen)
        
        # Configurar Tesseract
        config = r'--oem 3 --psm 6 -l spa+eng'
        
        # Extraer texto
        texto = pytesseract.image_to_string(imagen_procesada, config=config)
        texto_completo += texto + "\n"
        
    #print(texto_completo)
    
    return texto_completo

def extraer_datos_nombre_archivo(nombre_archivo):
    """Extrae número de resolución y nombre del estudiante SOLO del nombre del archivo.
    
    Formato esperado: 'RESOL. VADM - [numero de resolucion] [nombre de beneficiario].pdf'
    """
    datos = {
        'numero': None,
        'nombre_estudiante': None
    }
    
    # Patrón estricto para el formato específico
    patron = r'^RESOL\.\s+VADM\s*-\s*(\d+)\s+([A-ZÁÉÍÓÚÑ\s]+)(?:\.pdf)?$'
    match = re.match(patron, nombre_archivo, re.IGNORECASE)
    
    if match:
        datos['numero'] = f"VADM - {match.group(1).strip()}"  # Formato: "VADM - [numero de resolución]"
        datos['nombre_estudiante'] = match.group(2).strip().title()  # Formato nombre propio
    
    return datos

def procesar_resolucion(texto, nombre_archivo):
    """Extrae información clave de la resolución, obteniendo número y nombre SOLO del nombre del archivo"""
    # Primero extraer datos obligatorios del nombre del archivo
    datos = extraer_datos_nombre_archivo(nombre_archivo)
    
    if not datos['numero'] or not datos['nombre_estudiante']:
        raise ValueError("El nombre del archivo no sigue el formato esperado: 'RESOL. VADM - [NÚMERO] [NOMBRE].pdf'")
    
    # Completar con otros campos del texto del PDF
    datos.update({
        'cuerpo': None,
        'destinatarios': []
    })
    
    # 1. Normalizar texto para búsquedas
    texto = re.sub(r'\s+', ' ', texto).strip()
    
    # 2. Extraer el cuerpo del mensaje: el primer párrafo después del primer ")"
    cuerpo = None
    cierre_paren = texto.find(')')
    if cierre_paren != -1:
        texto_post_paren = texto[cierre_paren + 1:]
        
        # Buscar el primer párrafo (hasta salto de línea o punto y aparte)
        parrafo_match = re.search(r'([^\n\.]{20,300})', texto_post_paren)
        if parrafo_match:
            cuerpo = parrafo_match.group(1).strip()
            cuerpo = re.sub(r'\s+', ' ', cuerpo)  # Normalizar espacios
            datos['cuerpo'] = cuerpo
    
     # Extraer destinatarios
    seccion_correos = re.search(
        r'(Enviar copia|Notifíquese)(.*?)(?:\n\n|$)', 
        texto, re.IGNORECASE | re.DOTALL
    )
    
    if seccion_correos:
        correos = re.findall(r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}', seccion_correos.group(2))
        datos['destinatarios'] = list(set(correos))
    
    return datos

def procesar_nuevas_resoluciones():
    for archivo in os.listdir(CARPETA_RESOLUCIONES):
        if archivo.lower().endswith('.pdf'):
            ruta_pdf = os.path.join(CARPETA_RESOLUCIONES, archivo)
            try:
                print(f"\n{'='*50}")
                print(f"Procesando: {archivo}")
                
                # Extraer texto con OCR
                texto = extraer_texto_pdf(ruta_pdf)
                print("\nTexto extraído (primeras líneas):")
                
                # Procesar resolución
                datos = procesar_resolucion(texto, archivo)
                print("\nDatos extraídos:")
                for key, value in datos.items():
                    print(f"- {key}: {value}")
                
                if datos['numero'] and datos.get('destinatarios'):
                    enviar_correo_resolucion(datos, archivo)
                    shutil.move(ruta_pdf, os.path.join(CARPETA_PROCESADOS, archivo))
                    registrar_log(f"Procesado exitosamente: {archivo}")
                else:
                    error_msg = f"Datos incompletos en: {archivo}"
                    if not datos.get('destinatarios'):
                        error_msg += " - No se encontraron destinatarios"
                    registrar_log(error_msg, error=True)
            except Exception as e:
                error_msg = f"Error procesando {archivo}: {str(e)}"
                print(f"❌ {error_msg}")
                registrar_log(error_msg, error=True)
                import traceback
                traceback.print_exc()

def registrar_log(mensaje, error=False):
    """Registra un mensaje en el archivo de log."""
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tipo = "ERROR" if error else "INFO"
    linea = f"[{fecha_hora}] {tipo} - {mensaje}\n"
    
    nombre_log = datetime.now().strftime('%Y-%m-%d') + '.log'
    ruta_log = os.path.join(CARPETA_LOGS, nombre_log)
    
    with open(ruta_log, 'a', encoding='utf-8') as f:
        f.write(linea)

if __name__ == '__main__':
    procesar_nuevas_resoluciones()