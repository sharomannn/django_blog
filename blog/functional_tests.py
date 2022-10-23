from selenium import webdriver
import unittest


class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            '/home/roman/Python_prodjects/django_blog/blog/chromedriver/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_install(self):
        """Проверка тайтла на главной странице"""
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Установка прошла успешно! Поздравляем!',
                      self.browser.title)
        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
