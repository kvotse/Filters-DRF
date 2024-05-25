import django_filters
from .models import News, Category


class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Категория')
    is_published = django_filters.BooleanFilter(label='Опубликовано')

    class Meta:
        model = News
        fields = ['title', 'category', 'is_published', 'created_at']
