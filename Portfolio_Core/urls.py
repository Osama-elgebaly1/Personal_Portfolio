from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('send_message/',views.send_message,name='send message'),
    path('project/<int:pk>/',views.project_details,name='project_details')
]
