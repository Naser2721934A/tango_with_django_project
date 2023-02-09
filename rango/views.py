from django.shortcuts import render
from rango.models import Category, Page
from rango.models import Category
from rango.forms import CategoryForm
from django.shortcuts import redirect
def index(request):
    
    category_list = Category.objects.order_by('-likes')[:5]
    # page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    # context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context=context_dict)



def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)#.order_by('-views')
        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form =CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            
            return redirect('/rango/')
        else:
            print(form.errors)
            
    return render(request, 'rango/add_category.html', {'form': form})
        
        
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')

        if category:
            page = Page.objects.get_or_create(category=category, title=title, url=url)

            return redirect(f'/rango/category/{category_name_slug}/')
        else:
            return redirect('/rango/')

    return render(request, 'rango/add_page.html', {'category': category})

    
