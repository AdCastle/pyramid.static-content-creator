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
        bad_url = "https://www.badurl./"
        empty_content = url_load(bad_url)
        self.assertFalse(empty_content)

    def test_check_code(self):
        from snapshot import check_code
        from snapshot import url_load
        url = "https://www.example.com/"
        url_200 = url_load(url)
        # valid page
        self.assertEquals(check_code(url_200), 200)

    def test_grab_content(self):
        from snapshot import grab_content
        url = "https://www.example.com/"
        html = grab_content(url)
        self.assertTrue("<h1>Example Domain</h1>" in html)
