import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'static_content_creator')

    def test_url_load(self):
        from snapshot import url_load
        url = "https://www.example.com/"
        url_content = url_load(url)
        self.assertTrue(url_content)