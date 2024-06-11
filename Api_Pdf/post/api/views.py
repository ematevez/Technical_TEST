from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from post.models import Post
from post.api.serializers import PostSerilizer
from PyPDF2 import PdfReader

import smtplib
import ssl
from email.message import EmailMessage

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerilizer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()  # Guarda el objeto Post
        primeras_lineas = self.mostrar_primeras_30_lineas(instance.file.path)
        success, message = self.enviar_correo(instance.email, primeras_lineas)
        print("Aca estoy")
        if success:
            return Response({"success": True, "message": message}, status=201)
        else:
            
            return Response({"success": False, "message": "Failed to send email"}, status=500)

    def mostrar_primeras_30_lineas(self, file_path):
        primeras_30_lineas = ""
        try:
            # Extraer las primeras 30 líneas del PDF
            with open(file_path, 'rb') as f:
                pdf_reader = PdfReader(f)
                primera_pagina = pdf_reader.pages[0]
                primeras_30_lineas = '\n'.join(primera_pagina.extract_text().split('\n')[:30])
        except Exception as e:
            print("Ocurrió un error:", str(e))
        return primeras_30_lineas

    def enviar_correo(self, to_email, content):
        # Configurar el servidor SMTP
        email_sender = "ematevez@gmail.com"
        password = "deftveqwynlicjbw"
        
        # Crear el mensaje de correo
        mensaje = EmailMessage()
        mensaje['From'] = email_sender
        mensaje['To'] = to_email
        mensaje['Subject'] = 'PDF Extraído'
    
        # Añadir el contenido del mensaje
        mensaje.set_content(content)

        # Iniciar la conexión SMTP y enviar el mensaje
        try:
            # Enviar correo electrónico
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.send_message(mensaje)
            return True, f"The email has been successfully sent to {to_email}"
        except Exception as e:
            return False, str(e)
