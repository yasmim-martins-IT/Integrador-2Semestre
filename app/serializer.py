from rest_framework import serializers
from .models import Ambiente , Sensores , Historico
from django.contrib.auth.models import User

class AmbientesSerializer (serializers.ModelSerializer):
    class Meta :
        model = Ambiente
        fields = '__all__'

class SensorSerializer (serializers.ModelSerializer) :
    class Meta : 
        model = Sensores
        fields = '__all__'
class HistoricoSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Historico
        fields = '__all__'
class UserSerializer (serializers.ModelSerializer) :
    #serializer para autentificação
    class Meta :
        model = User
        fields = ['username' , 'password'] #pega somente esses campos especificos
        extra_kwards = {'password': {'write_only' : True}} # ninguém pode ver a senha

    def create(self, validated_data):
        return User.objects.create_user(**validated_data) #cria o super user

