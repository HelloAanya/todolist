from django.contrib import admin
from django.urls import path, include
from . import views as app_views  # Corrected import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', app_views.login_view, name='login'),  # Use app_views consistently
    path('signup/', app_views.signup_view, name='signup'),  # Use app_views consistently
    path('home/', app_views.home_view, name='home'), 
    path('', app_views.first_view, name='first'),
    path('create_task/', app_views.create_task_page, name='create_task'),
    path('logout/', app_views. custom_logout, name='logout'),
    path('delete_task/<int:task_id>/', app_views.delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', app_views.update_task, name='update_task'),
    
    
]
