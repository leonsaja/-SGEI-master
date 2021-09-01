from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts.views import user_admin_view, user_view
from accounts.forms.form_user import LoginForm

app_name='accounts'

urlpatterns = [

    #admininstrador
    path('criar_usuario_admin/', user_admin_view.CriarUsuarioAdminView.as_view(), name='criar_usuario_admin'),
    path('listar/', user_admin_view.ListarUsuariosView.as_view(), name='listar_usuarios'),

    #usuario
    path('criar_usuario/', user_view.CriarUsuarioView.as_view(), name='criar_usuario'),
    path('atualizar_perfil/', user_view.perfil_user, name='atualizar_perfil'),
    path('editar/<int:pk>', user_view.EditarUsuarioView.as_view(), name='editar_usuario'),
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