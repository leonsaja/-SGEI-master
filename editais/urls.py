from django.urls import path
from editais.views import edital_views


app_name ='edital'

urlpatterns = [
    path('cadastrar/', edital_views.CriarEditalView.as_view(), name='criar_edital'),
    path('editar/<int:pk>/', edital_views.EditarEditalView.as_view(), name='editar_edital'),
    path('listar/', edital_views.ListarEditalView.as_view(), name='listar_editais'),
    path('detalhe/<int:pk>/',edital_views.DetalheEditalView.as_view(),name='edital_detalhe'),
    path('remover/<int:pk>/', edital_views.RemoverEditalView.as_view(), name='remover_edital'),


]