"""rest_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import restapp.views
from restapp.views import home,RegisterView,Reservation,LoginView,update


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',restapp.views.home, name = 'home'),
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('reservation/',restapp.views.reservation, name = 'reservation'),
    path('update/<int:reservation_id>',restapp.views.update,name = 'update'),
    path('update/<int:reservation_id>/delete',restapp.views.delete,name = 'delete')
]
