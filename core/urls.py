from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndexView, CategoryView, RedirectView, SimpleForm, NewsListView, NewsViewSet, NewsAPIView

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('redirect/', RedirectView.as_view(), name='redirect'),
    path('form/', SimpleForm.as_view(), name='form'),
    path('news-list/', NewsListView.as_view(), name='news_list'),  # Изменено имя URL для списка новостей
    path('api/', include(router.urls)),  # Добавление маршрутов для REST API
    path('api/news/', NewsAPIView.as_view(), name='news_api'),  # Новый маршрут для NewsAPIView
]
