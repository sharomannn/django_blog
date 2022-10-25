from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By



class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            '/home/roman/Python_prodjects/django_blog/blog/chromedriver/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # В заголовке сайта вася прочитал Шарипов Роман
        """Проверка тайтла на главной странице"""
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Шарипов Роман',
                      self.browser.title)

    def test_home_page_header(self):
        # В хедере сайта вася прочитал Шарипов Роман
        """Проверка хедера на главной странице"""
        self.browser.get('http://127.0.0.1:8000/')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Шарипов Роман',
                      header.text)

    def test_home_page_blog(self):
        # Под шапкой расположен блок со статьями
        """Проверка наличия блога на главной странице"""
        self.browser.get('http://127.0.0.1:8000/')
        article_list = self.browser.find_element_by_class_name('article-list')
        self.assertTrue(article_list)

    def test_home_page_blog_articles(self):
        """Проверка наличия контента в блоге"""
        self.browser.get('http://127.0.0.1:8000/')
        article_title = self.browser.find_element_by_class_name('article-title')
        article_summary = self.browser.find_element_by_class_name('article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

if __name__ == '__main__':
    unittest.main()

# Жил был вася
# Вася учит программирование и хочет изучить django
# Вася открыл сайт

# В заголовке сайта вася прочитал Шарипов Роман
# Под шапкой расположен блок со статьями

# У каждой статьи есть заголовок и один абзац с текстом
