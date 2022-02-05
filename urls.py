"""Young_stunners_general_category URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from upload import views as views_upload
from transfer import views as views_transfer
from users import views as views_users
from check import views as views_check
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload',views_upload.upload_view),
    path('transfer',views_transfer.transfer_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register',views_users.register_view),
    path('',views_users.home),
    path('check',views_check.check)

]
