# Automatización de Envío de Correos para Resoluciones

Esta aplicación procesa automáticamente resoluciones en PDF y envía correos electrónicos con la información extraída.

## Instrucciones de uso

1. Instalar las dependencias:

pip install -r requirements.txt


2. Configurar el servidor SMTP en `config.py` con las credenciales correctas.

3. Colocar los PDFs de las resoluciones en la carpeta `/resoluciones_pdf/`.

4. Ejecutar el script principal:

python procesador_resoluciones.py


5. Los PDFs procesados se moverán a la carpeta `/procesados/` y los logs se guardarán en `/logs/`.

## Notas

- La aplicación busca información específica en las resoluciones (número, fecha, nombre del estudiante, etc.).
- Los correos se envían a las direcciones encontradas en el "ARTÍCULO CUARTO" de cada resolución.
- Revisar los logs en caso de errores.