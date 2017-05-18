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
    tags = models.CharField(max_length=80, blank=True)
    published = models.BooleanField(default=True)
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


class Ad(models.Model):
    title = models.CharField(verbose_name='Nome da Empresa', blank=False, null=False,
                             max_length=250)
    image = models.ImageField(upload_to='anuncios/images',
                              verbose_name='Imagem da Empresa',
                              null=False, blank=False)
    status = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anúncio de Empresa'
        verbose_name_plural = 'Anúncios de Empresas'
        ordering = ['-title']

class About(models.Model):
    summary = models.CharField(verbose_name='Resumo', blank=False, max_length=250)
    content = RichTextUploadingField(verbose_name='Conteúdo', blank=False)
    image_capa = models.ImageField(upload_to='about/images',
                              verbose_name='Imagem da Capa',
                              null=True, blank=True)

    def __str__(self):
        return self.summary

    class Meta:
        verbose_name = 'Sobre Neuly'
        verbose_name_plural = 'Sobre Neuly'
        ordering = ['-summary']

class Banner(models.Model):
    title = models.CharField(blank=False, max_length=100)
    image_banner = models.ImageField(upload_to='banner/images',
                              verbose_name='Imagem de Início',
                              null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Banner Início'
        verbose_name_plural = 'Banner Início'
        ordering = ['-title']
