from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import ProductForm, ProjectForm, CustomAuthenticationForm
from .models import Product, Project
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'app/home.html')
    else:
        return redirect('app:login')
    
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app:home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('app:login')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'app/list.html', {'object_list': projects, 'title':'Список проектов', 'edit_url': 'project', 'create_url': 'new_project'})

def project(request, project_id=None):
    if project_id:
        project = get_object_or_404(Project, id=project_id)
        form = ProjectForm(request.POST or None, instance=project)
    else:
        form = ProjectForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app:projects')
    return render(request, 'app/edit.html', {'form': form})




    
def products(request):
    products = Product.objects.all()
    return render(request, 'app/list.html', {'object_list': products, 'title': 'Список наименований', 'edit_url': 'product', 'create_url': 'new_product'})

def product(request, product_id=None):
    if product_id:
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(request.POST or None, instance=product)
    else:
        form = ProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app:products')
    return render(request, 'app/edit.html', {'form': form})
    


def project_spec(request, project_id):
    project = get_object_or_404(Project, id = project_id)
    products = Product.objects.filter(projects=project).prefetch_related('projects')
    existing_products = Product.objects.all()

    context = {
        'project': project,
        'products': products,
        'existing_products': existing_products,
    }

    return render(request, 'app/project_spec.html', context)

def add_product_to_the_project(request, product_id, project_id):
    product = get_object_or_404(Product, id = product_id)
    project = get_object_or_404(Project, id = project_id)
    product.projects.add(project)
    return HttpResponseRedirect(reverse('app:project_spec', args=(project_id,)))

def rem_product_from_the_project(request, product_id, project_id):
    product = get_object_or_404(Product, id = product_id)
    project = get_object_or_404(Project, id = project_id)
    product.projects.remove(project)
    return HttpResponseRedirect(reverse('app:project_spec', args=(project_id,)))