from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def doctors(request):
    return render(request, 'doctors.html')


def services(request):
    return render(request, 'services.html')


def department(request):
    return render(request, 'department.html')


def pricing(request):
    return render(request, 'pricing.html')


def gallery(request):
    return render(request, 'gallery.html')


def blogsingle(request):
    return render(request, 'blogsingle.html')
