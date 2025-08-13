📧 AutoResolutions-toEmail
Aplicación para procesar automáticamente resoluciones en PDF y enviar correos electrónicos con la información extraída de forma rápida y confiable.

🚀 Características principales
📄 Lectura automática de resoluciones en PDF.

🔍 Extracción de datos clave: número de resolución, fecha, nombre del estudiante, artículos relevantes, etc.

✉️ Generación y envío de correos con asunto y cuerpo personalizados.

🗂 Organización automática de PDFs procesados.

📝 Registro detallado en logs para auditoría y diagnóstico.

📦 Instalación y configuración

1️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

2️⃣ Configurar el entorno
Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

env
Copiar
Editar
# Configuración SMTP (Ejemplo: Gmail)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=tu_correo@dominio.com
SMTP_PASSWORD=tus_credenciales_o_app_password
SMTP_FROM_EMAIL=tu_correo@dominio.com
SMTP_SUBJECT_PREFIX=COMUNICACIÓN RESOLUCIÓN {numero} DEL 2025

# Destinatarios (múltiples separados por comas)
EMAIL_RECIPIENTS=correo1@ejemplo.com,correo2@ejemplo.com
Notas:

Para Gmail con verificación en dos pasos, utiliza una Contraseña de aplicación.

No subas tu archivo .env al repositorio (ya está en .gitignore).

3️⃣ Preparar carpetas y archivos
Asegúrate de que existan las carpetas necesarias:

```bash
/resoluciones_pdf/   # PDFs a procesar
/procesados/         # PDFs procesados
/logs/               # Archivos de registro
Coloca los PDFs a procesar dentro de /resoluciones_pdf/.
```

▶️ Ejecución
```bash
python procesador_resoluciones.py
```

📊 Resultados

Los PDFs procesados se moverán automáticamente a /procesados/.

Los registros de ejecución se guardarán en /logs/.

Los correos se enviarán a los destinatarios definidos en .env.

🧠 Funcionamiento interno

Lectura de PDF y búsqueda de datos:

Número y fecha de la resolución.

Nombre del estudiante.

Artículos relevantes.

Correos extraídos del ARTÍCULO CUARTO.

Generación de correo:

Asunto automático con el número de resolución.

Saludo dinámico según la hora del día.

Cuerpo del mensaje con formato estandarizado.

Firma institucional.

Envío y registro:

Se envía el correo a los destinatarios.

Se registra la operación en logs.

El PDF se mueve a la carpeta de procesados.

⚠️ Recomendaciones
Seguridad: No compartas tu .env ni tus credenciales.

Pruebas: Ensaya primero con 1 o 2 PDFs antes de procesar lotes grandes.

Personalización: Modifica enviar_correo.py para cambiar la plantilla del mensaje.

Logs: Revisa /logs/ si ocurre algún error.

📂 Estructura del proyecto

/automatizacion-resoluciones/
├── /resoluciones_pdf/           # PDFs a procesar
├── /procesados/                 # PDFs procesados
├── /logs/                       # Registros de ejecución
├── .env                         # Configuración sensible (NO SUBIR)
├── config.py                    # Configuración de rutas
├── enviar_correo.py             # Lógica de envío de correos
├── procesador_resoluciones.py   # Script principal
├── requirements.txt             # Dependencias
└── README.md                    # Este archivo

🛠 Soporte
Si encuentras un problema:

Revisa los logs en /logs/.

Abre un issue en el repositorio con el detalle del error.