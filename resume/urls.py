
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('about',views.about, name='about'),
    path('projects',views.projects, name='projects'),
    path('experience',views.experience, name='experience'),
    path('contact',views.contact, name='contact'),
    path('resume',views.resume, name='resume'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)