from django.urls import path,include

from django.contrib.auth import views as auth_views # el modulo que contiene a la vista basada en clases
# que nos mostrará el formulario para iniciar sesion

from . import views

app_name="user"
urlpatterns = [
	path('',views.home,name="home"),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/',views.register, name="register")
    



]
