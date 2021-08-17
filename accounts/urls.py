from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts.views import user_view as user_views,user_admin_view as admin_views
from .forms.form_user import LoginForm

app_name='accounts'

urlpatterns = [
    path('criar_usuario/',user_views.criar_usuario,  name='criar_usuario'),
    path('criar_usuario_admin/', admin_views.criar_usuario_admin, name='criar_usuario_admin'),
    path('atualizar_perfil/', user_views.perfil_user, name='atualizar_perfil'),
    path('editar/<int:id>', user_views.editar_usuario, name='editar_usuario'),
    path('listar/', user_views.listar_usuarios, name='listar_usuarios'),
    path('login/', auth_views.LoginView.as_view(form_class=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    #redefinir a senha
    path('alterar_senha', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('core:index')), name='alterar_senha'),
    path('resetar_senha', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')),
         name='resetar_senha'),
    path('resetar_senha/sucesso', auth_views.PasswordResetCompleteView.as_view(),
         name='resetar_senha_sucesso'),
    path('resetar_senha/<str:uidb64>/<str:token>',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:resetar_senha_sucesso')),
         name='password_reset_confirm'),
    path('resetar_senha/feito', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

]