from django.db import models
# Create your models here.
class Ambiente (models.Model) :
    sig = models.IntegerField(unique=True) #campo unico de identificação para o ambiente
    descricao = models.CharField(max_length=200)
    ni = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sig} - {self.descricao}"


class Sensores (models.Model) :
    TIPOS_CHOICES = [('temperatura' , 'Temperatura') , ('umidade', 'Umidade'), ('luminosidade', 'Luminosidade') , ('contador', 'Contador')]

    sensor = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30,choices=TIPOS_CHOICES)
    mac_address = models.CharField(max_length=20 )
    unidade_med = models.CharField(max_length=20)
    latitude = models.CharField(max_length=100)
    longitude = models.FloatField()
    status = models.BooleanField(default= True)

    def __str__(self):
        return self.sensor 

class Historico (models.Model):
    sensor = models.ForeignKey(Sensores ,on_delete=models.CASCADE ) #chave estrangeira referenciando Sensores
    ambiente = models.ForeignKey(Ambiente , on_delete=models.CASCADE) # chave estrangeira referenciando Ambiente
    valor = models.FloatField()
    timestamp = models.IntegerField()

    def __str__(self):
        return f"{self.sensor} - {self.timestamp}"

