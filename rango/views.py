from django.shortcuts import render
from rango.models import Category, Page
from rango.models import Category
from rango.forms import CategoryForm
from django.shortcuts import redirect
from rango.forms import PageForm
from django.urls import reverse
from django.shortcuts import render

def index(request):
    context_dict = {}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'rango/about.html', context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
    return render(request, 'rango/category.html', context_dict)

def add_category(request):
    context_dict = {}
    return render(request, 'rango/add_category.html', context_dict)

def add_page(request, category_name_slug):
    context_dict = {}
    return render(request, 'rango/add_page.html', context_dict)
