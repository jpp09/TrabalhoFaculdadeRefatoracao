from django.db import models
from datetime import datetime
import django.utils.timezone as time
from django.contrib.auth.models import User

class comentarios(models.Model):
    comentario = models.CharField(max_length=250,null=False,blank=False,default='')
    data_publicacao = models.DateField(default=time.now())
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)