from django.urls import path

from frontoffice import views

app_name = 'map'

urlpatterns = [
    path('', views.index, name='admin_panel_cabinet'),
]
