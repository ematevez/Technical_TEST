from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from post.models import Post
from post.api.serializers import PostSerializer
from PyPDF2 import PdfReader
import smtplib
import ssl
from email.message import EmailMessage

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            instance = serializer.save()
            primeras_lineas = self.mostrar_primeras_30_lineas(instance.file.path)
            success, message = self.enviar_correo(instance.email, primeras_lineas)
            if success:
                data = {"success": True, "message": message}
                status_code = status.HTTP_201_CREATED
            else:
                data = {"success": False, "message": message}
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            data = {"success": False, "message": "Invalid data provided"}
            status_code = status.HTTP_400_BAD_REQUEST
        
        return Response(data, status=status_code)

    def mostrar_primeras_30_lineas(self, file_path):
        primeras_30_lineas = ""
        try:
            with open(file_path, 'rb') as f:
                pdf_reader = PdfReader(f)
                primera_pagina = pdf_reader.pages[0]
                primeras_30_lineas = '\n'.join(primera_pagina.extract_text().split('\n')[:30])
        except Exception as e:
            print("Ocurrió un error:", str(e))
        return primeras_30_lineas

    def enviar_correo(self, to_email, content):
        email_sender = "ematevez@gmail.com"
        password = "deftveqwynlicjbw"
        mensaje = EmailMessage()
        mensaje['From'] = email_sender
        mensaje['To'] = to_email
        mensaje['Subject'] = 'PDF Extraído'
        mensaje.set_content(content)
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.send_message(mensaje)
            return True, f"The email has been successfully sent to {to_email}"
        except Exception as e:
            return False, str(e)
