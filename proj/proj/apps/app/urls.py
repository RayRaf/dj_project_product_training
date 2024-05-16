from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('new_project/', views.project, name='new_project'),
    path('project_spec/<int:project_id>/', views.project_spec, name='project_spec'),
    path('products/', views.products, name='products'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('new_product/', views.product, name='new_product'),
    path('add_product/<int:product_id>/to_the_project/<int:project_id>/', views.add_product_to_the_project, name='add_product_to_the_project'),
    path('rem_product/<int:product_id>/from_the_project/<int:project_id>/', views.rem_product_from_the_project, name='rem_product_from_the_project'),
]