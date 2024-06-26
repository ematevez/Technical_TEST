# Instrucciones de Uso - Proyecto Technical_TEST

Este repositorio contiene un proyecto desarrollado como parte de una prueba técnica. Aquí encontrarás una API Django que te permite procesar archivos PDF y enviar contenido por correo electrónico.

## Descarga del Proyecto

1. Abre tu terminal (o línea de comandos).

2. Clona el repositorio desde GitHub:

   git clone https://github.com/ematevez/Technical_TEST.git

## Instalación de Django y Migraciones
  Asegúrate de tener Python y pip instalados en tu sistema.

  Navega a la carpeta del proyecto:

         cd Api_django
  
  Realiza las migraciones de la base de datos:
        
        python manage.py makemigrations
        python manage.py migrate

  Instalación de Requirements

    Instala las dependencias del proyecto:
      
         pip install -r requirements.txt

Utilización de la API
Ejecuta el servidor Django:

    python manage.py runserver

Abre tu navegador web y accede a la siguiente URL para ver la  API:

    http://127.0.0.1:8000/

Abre tu navegador web y accede a la siguiente URL para ver la documentación de la API (swagger):
No se finalizo por que no tiene muchas funcionalidades.
   
      http://127.0.0.1:8000/docs
    
      http://127.0.0.1:8000/redocs
        

![alt text](image-3.png)

![alt text](image-4.png)

Descripcion del proyecto
   Este repositorio contiene un proyecto desarrollado como parte de una prueba técnica. 
   Aquí encontrarás una API Django que te permite procesar archivos PDF y enviar el contenido de las primeras 30 líneas al destinatario ingresado en la API.

Subida de Archivos PDF
   Cuando se sube un archivo PDF, el software extrae automáticamente las primeras 30 líneas del archivo, 
   lo cual puede variar dependiendo del formato de la hoja configurada en el archivo. 
   Estas líneas se envían al destinatario especificado en la API.

   Es importante tener en cuenta que si se visualiza la información en un smartphone u otro dispositivo, podrían mostrarse más líneas, 
   pero estas están seleccionadas en función del formato de la hoja configurada en el archivo PDF.


Consulta GET

![alt text](image-1.png)

Post 

![alt text](image.png)

Correo enviado 

![alt text](image-2.png)

Acerca del Desarrollador
¡Hola! Soy Emanuel Tevez, el desarrollador detrás de este proyecto. Si tienes alguna pregunta, sugerencia o simplemente quieres conectar, ¡no dudes en ponerte en contacto conmigo!

Este repositorio contiene un proyecto desarrollado como parte de una prueba técnica. Si bien una prueba técnica puede demostrar los conocimientos de un desarrollador en un instante específico, es importante reconocer que va más allá de unas simples líneas de código.

Para demostrar lo que soy y lo que puedo aportar, estoy dispuesto a trabajar de manera gratuita por un tiempo prudencial. De esta manera, podrán conocerme mejor y ver el valor que puedo aportar más allá de las habilidades técnicas, la experiencia en el campo y la facilidad de desempeñarme bajo presión.

Les agradezco la oportunidad y espero que pueda trabajar con uds.
Perfil de LinkedIn
linkedin https://www.linkedin.com/in/emanuel-juli%C3%A1n-tevez
