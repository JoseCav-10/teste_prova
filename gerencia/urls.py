from django.urls import path
from .views import inicio_gerencia, listagem_noticia,cadastrar_noticia,editar_noticia,CategoriaListView, CategoriaCreateView, CategoriaDeleteView, CategoriaUpdateView

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('nova_categoria/', CategoriaCreateView.as_view(), name='cre'),
    path('editar_categoria/<int:pk>/', CategoriaUpdateView.as_view(), name='upd'),
    path('excluir_categoria/<int:pk>/', CategoriaDeleteView.as_view(), name='del'),
    path('categoria/', CategoriaListView.as_view(), name='list_categoria'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia')
    # Add your URL patterns here
]