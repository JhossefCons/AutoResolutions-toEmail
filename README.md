# AutoResolutions-toEmail

Esta aplicación procesa automáticamente resoluciones en PDF y envía correos electrónicos con la información extraída.

## 📋 Instrucciones de uso

1. Instalar las dependencias:

pip install -r requirements.txt

2. Configuración del entorno
Configuración del archivo .env
Crea un archivo .env en la raíz del proyecto con las siguientes variables:

# Configuración SMTP (Ejemplo para Gmail)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=tu_correo@dominio.com
SMTP_PASSWORD=tus_credenciales_o_app_password
SMTP_FROM_EMAIL=tu_correo@dominio.com
SMTP_SUBJECT_PREFIX=COMUNICACIÓN RESOLUCION {numero} DEL 2025

# Destinatarios (separar múltiples correos con comas)
EMAIL_RECIPIENTS=correo1@ejemplo.com,correo2@ejemplo.com

Notas importantes:

Para Gmail, necesitarás una "Contraseña de aplicación" si usas verificación en dos pasos

Nunca subas el archivo .env al repositorio (está incluido en .gitignore)

3. Preparación de archivos
Coloca los PDFs de las resoluciones en la carpeta /resoluciones_pdf/.

4. Ejecución del sistema
bash
python procesador_resoluciones.py
5. Resultados
Los PDFs procesados se moverán a /procesados/

Los logs detallados se guardarán en /logs/

# 🔍 Funcionamiento interno de La aplicación:

Busca información específica en las resoluciones:

Número de resolución

Fecha de emisión

Nombre del estudiante

Artículos relevantes

Procesa el "ARTÍCULO CUARTO" para extraer direcciones de correo

Genera y envía correos con:

Asunto automático con número de resolución

Saludo según hora del día (Buenos días/tardes)

Cuerpo del mensaje estandarizado

Firma institucional

# ⚠️ Notas importantes 

Seguridad: Nunca compartas tu archivo .env

Logs: Revisa /logs/ para diagnóstico de errores

Pruebas: Verifica con 1-2 resoluciones antes de procesar lotes grandes

Personalización: Puedes modificar las plantillas de correo en enviar_correo.py

# 📂 Estructura del proyecto

/automatizacion-resoluciones/
├── /resoluciones_pdf/    # PDFs a procesar
├── /procesados/          # PDFs ya procesados
├── /logs/                # Registros de ejecución
├── .env                  # Configuración sensible (NO SUBIR)
├── config.py             # Configuración de rutas
├── enviar_correo.py      # Lógica de envío de emails
├── procesador_resoluciones.py # Script principal
├── requirements.txt      # Dependencias
└── README.md             # Este archivo

# 🛠 Soporte
Para problemas técnicos, revisa los logs o abre un issue en el repositorio.