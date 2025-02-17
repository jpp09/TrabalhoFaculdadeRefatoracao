from django.urls import path
from conteudo.views import index,login,register,logout,comunidade


urlpatterns = [
    path('',index,name='index'),
    path('login',login,name='login'),
    path('register',register,name='register'),
    path('logout',logout,name='logout'),
    path('comunidade',comunidade,name='comunidade')
]