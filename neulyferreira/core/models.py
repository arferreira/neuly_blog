from django.db import models
# ckeditor
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    title = models.CharField('Título', max_length=250)
    slug = models.SlugField('Atalho')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-title']


class Post(models.Model):
    title = models.CharField('Título', max_length=250)
    slug = models.SlugField('Atalho')
    content = RichTextUploadingField('Conteúdo', blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    author = models.CharField('Autor', max_length=100)
    image_capa = models.ImageField(upload_to='posts/images',
                              verbose_name='Imagem da Capa',
                              null=True, blank=True)
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-title']
