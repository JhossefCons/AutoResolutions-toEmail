import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_CONFIG

def enviar_correo_resolucion(datos_resolucion, Archivo):
    hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
    print('Hora actual:', hora_actual)
    
    if hora_actual <= '08:00:00' <= '11:59:59':
        saludo = "Buenos días"
    elif '12:00:00' <= hora_actual <= '17:59:59':
        saludo = "Buenas tardes"
        
    try:
        Texto_Correo = f"""
        {saludo},
        
        Apreciados Universitarios,
        
        Asunto : {datos_resolucion['cuerpo']}
        
        Cordial saludo,
        
        De manera respetuosa remito las Resolución {datos_resolucion['numero']} de ______ de 2025 para su conocimiento.
        
        Universitariamente,

        MIRTA LUCIA QUINTERO BOLAÑOS

        Apoyo Administrativo
        -- 
        VICERRECTORÍA ADMINISTRATIVATelf. 8209900 Ext. 1121-1122-1124-1130
        Calle 4#5-30 Edificio Administrativo
            """
        
        msg = MIMEMultipart()
        msg['From'] = SMTP_CONFIG['from_email']
        msg['To'] = ', '.join(['niconstain@gmail.com'])
        msg['Subject'] = SMTP_CONFIG['subject_prefix'].format(numero=datos_resolucion['numero'])
        msg.attach(MIMEText(Texto_Correo, 'plain'))
        
        # Enviar con SMTP
        with smtplib.SMTP(SMTP_CONFIG['server'], SMTP_CONFIG['port']) as server:
            server.starttls()
            server.login(SMTP_CONFIG['username'], SMTP_CONFIG['password'])
            server.send_message(msg)
            print("✅ Correo generado y enviado")

    except Exception as e:
        print(f"❌ Error: {str(e)}")