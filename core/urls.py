from django.urls import path
from .views import index, contact, about, blog, doctors, services, department, pricing, gallery, blogsingle

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('doctors', doctors, name='doctors'),
    path('services', services, name='services'),
    path('department', department, name='department'),
    path('pricing', pricing, name='pricing'),
    path('gallery', gallery, name='gallery'),
    path('blogsingle', blogsingle, name='blog-single'),

]
