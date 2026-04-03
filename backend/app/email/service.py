# app/email/service.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader, select_autoescape
from fastapi import BackgroundTasks
from app.core.config import settings
from pathlib import Path

# Ruta absoluta a las plantillas (más confiable)
TEMPLATES_DIR = Path(__file__).parent.parent.parent /"app"/ "templates" / "email"

env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape(['html', 'xml'])
)

def send_email_background(
    background_tasks: BackgroundTasks,
    to_email: str,
    subject: str,
    template_name: str,      # debe incluir .html
    context: dict
):
    background_tasks.add_task(
        send_email_sync, to_email, subject, template_name, context
    )


def send_email_sync(to_email: str, subject: str, template_name: str, context: dict):
    try:
        # Cargar plantilla
        template = env.get_template(template_name)
        html_content = template.render(**context)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"{settings.EMAIL_FROM_NAME} <{settings.EMAIL_FROM}>"
        msg["To"] = to_email

        msg.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
            server.sendmail(settings.EMAIL_FROM, to_email, msg.as_string())

        print(f"✅ Email enviado exitosamente a {to_email} | Template: {template_name}")
        
    except Exception as e:
        print(f"❌ Error enviando email a {to_email}: {str(e)}")
        # Opcional: puedes loguear el error en un archivo o sistema de logs