from django.urls import resolve
from django.test import TestCase
from blog.views import home_page
from blog.models import Article
from django.http import HttpRequest
from datetime import datetime


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Шарипов Роман</title>', html)
        self.assertTrue(html.endswith('</html>'))


class ArticleModelTest(TestCase):
    def test_article_creation_and_save(self):
        """Создание и сохранение статьи"""
        article1 = Article(
            title='article 1',
            full_text='full_text 1',
            summary='summary 1',
            created=datetime.now(),
            updated=datetime.now(),
        )
        article1.save()

        article2 = Article(
            title='article 2',
            full_text='full_text 2',
            summary='summary 2',
            created=datetime.now(),
            updated=datetime.now(),
        )

        article2.save()
        all_article = Article.objects.all()
        self.assertEqual(len(all_article), 2)
        self.assertEqual(
            all_article[0].title,
            article1.title
        )
        self.assertEqual(
            all_article[1].title,
            article2.title
        )
