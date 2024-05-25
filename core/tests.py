from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import News, Category

class NewsTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(title='TestCategory')
        self.news_data = {
            'title': 'Test News',
            'content': 'This is a test news content.',
            'is_published': True,
            'category': self.category  # Здесь нужно передавать экземпляр Category
        }
        self.news = News.objects.create(**self.news_data)

    def test_list(self):
        url = reverse('news-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_detail(self):
        url = reverse('news-detail', args=[self.news.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.news.title)

    def test_create(self):
        url = reverse('news-list')
        data = {
            'title': 'New Test News',
            'content': 'This is another test news content.',
            'is_published': True,
            'category': self.category.id  # Используем id для создания через API
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 2)
        self.assertEqual(News.objects.get(id=response.data['id']).title, 'New Test News')

    def test_update(self):
        url = reverse('news-detail', args=[self.news.id])
        data = {
            'title': 'Updated Test News',
            'content': 'Updated content.',
            'is_published': True,
            'category': self.category.id  # Используем id для обновления через API
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.news.refresh_from_db()
        self.assertEqual(self.news.title, 'Updated Test News')

    def test_partial_update(self):
        url = reverse('news-detail', args=[self.news.id])
        data = {
            'title': 'Partially Updated Test News'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.news.refresh_from_db()
        self.assertEqual(self.news.title, 'Partially Updated Test News')

    def test_delete(self):
        url = reverse('news-detail', args=[self.news.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(News.objects.count(), 0)
