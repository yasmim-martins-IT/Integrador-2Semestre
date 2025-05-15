from django.shortcuts import render
from .models import Ambiente , Sensores , Historico
from .serializer import UserSerializer , Ambiente , Historico , Sensores
import pandas as pd
import csv
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.views  import TokenObtainPairView
""" 
    Essa página contém as views 
    Foi utilizado dois recursos do django para fazer :
    -Decorators
    -ClassBase
"""
class LoginView (TokenObtainPairView) :
    serializer_class =  UserSerializer




# Create your views here.
