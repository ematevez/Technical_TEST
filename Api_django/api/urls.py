from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('', Post_APIView.as_view()), 
    path('/<int:pk>/', Post_APIView_Detail.as_view()),
    
]