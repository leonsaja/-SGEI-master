from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from .views import criar_usuario,editar_usuario
from .forms.form_user import LoginForm
from django.contrib.auth.views import PasswordChangeView

app_name='accounts'

urlpatterns = [
    path('login',LoginView.as_view(form_class=LoginForm),name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('criar', criar_usuario,  name='criar_usuario'),
    path('editar/<int:id>', editar_usuario, name='editar_usuario'),
    path('alterar_senha', PasswordChangeView.as_view(success_url=reverse_lazy('core:index')), name='alterar_senha'),
]