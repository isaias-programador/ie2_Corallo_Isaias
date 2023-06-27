from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Q
from model_utils import Choices


ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'titulo'),
    ('2', 'genero'),
    ('3', 'created_at'),
    ('4', 'updated_at'),
)


class libros(models.Model):
    titulo = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'libros'
        ordering = ("titulo",)
        verbose_name = "libro"
        verbose_name_plural = "libros"


    def __str__(self):
        return self.titulo


def query_libros_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]


    order_column = ORDER_COLUMN_CHOICES[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column


    queryset = libros.objects.all()
    total = queryset.count()


    if search_value:
        queryset = queryset.filter(Q(id__icontains=search_value) |
                                        Q(titulo__icontains=search_value) |
                                        Q(genero__icontains=search_value) |
                                        Q(created_at__icontains=search_value) |
                                        Q(updated_at__icontains=search_value))


    count = queryset.count()


    if length == -1:
        queryset = queryset.order_by(order_column)
    else:
        queryset = queryset.order_by(order_column)[start: start + length]


    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }
