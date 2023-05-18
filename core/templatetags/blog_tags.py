from django import template
from core.models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.publicados.count()


@register.inclusion_tag('blog/index.html')
def mostrar_ultimos_posts(count=5):
    posts = Post.publicados.order_by('-publicado')[:count]
    return {'ultimos': posts}