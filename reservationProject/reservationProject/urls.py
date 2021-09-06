from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from reservationApp import views as reservationAppViews

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^reservation/', include('reservationApp.urls')),
    url(r'^$',reservationAppViews.HomePage, name="homepage"),
]
