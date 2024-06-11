from django.db import models


class Post(models.Model):
    email = models.EmailField()
    file = models.FileField(blank='', default='',upload_to='archivos_pdf/')
    def __str__(self):
        return self.correo

