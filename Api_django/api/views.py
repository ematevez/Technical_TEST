from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import PostSerializers
from .models import Post
from rest_framework import status
from django.http import Http404
import os
from django.conf import settings
from PyPDF2 import PdfReader

import smtplib
import ssl
from email.message import EmailMessage
    
class Post_APIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request, format=None, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializers(post, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            route = "media/archivos_pdf/" + str(serializer.validated_data.get('file'))
            cuerpo= self.mostrar_primeras_30_lineas(route)
            serializer.save()
            success, message = self.enviar_correo(email,cuerpo)
            return Response({"success": success, "message": message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    
    
    def enviar_correo(self, to_email, cuerpo):  # falta el contenido
        email_sender = "ematevez@gmail.com"
        password = "deftveqwynlicjbw"
        mensaje = EmailMessage()
        mensaje['From'] = email_sender
        mensaje['To'] = to_email
        mensaje['Subject'] = 'PDF Extraído'
        mensaje.set_content(cuerpo)
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.send_message(mensaje)
            return True, f"The email has been successfully sent to {to_email}"
        except Exception as e:
            return False, str(e)

class Post_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"Error"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
