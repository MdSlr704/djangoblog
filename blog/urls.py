from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage),
    path('newpost/',views.new_post),
    path('<int:id>/edit/',views.edit_post),
    path('<int:id>/delete/',views.delete_post),
]
