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
        broken_url = "https://www.example."
        broken_html = grab_content(broken_url)
        self.assertFalse(broken_html)

    def test_remove_domain_from_url(self):
        from snapshot import remove_domain_from_url
        url = "https://www.example.com/path/to/file"
        path_to_file = remove_domain_from_url("example.com/", url)
        self.assertEqual(path_to_file, "path/to/file")
        path_to_file = remove_domain_from_url("example.com", url)
        self.assertEqual(path_to_file, "/path/to/file")
        path_to_file = remove_domain_from_url("examle.com", url)
        self.assertEqual(path_to_file, None)

    def test_split_url_to_path(self):
        from snapshot import split_url_to_path
        from snapshot import remove_domain_from_url
        url = "https://www.example.com/path/to/file"
        path_to_file = remove_domain_from_url("example.com/", url)
        path = split_url_to_path(path_to_file)
        self.assertEqual(path, ['path', 'to', 'file'])
        url = "https://www.example.com/path/to/file/"
        path_to_file = remove_domain_from_url("example.com/", url)
        path = split_url_to_path(path_to_file)
        self.assertEqual(path, ['path', 'to', 'file'])

    def test_does_file_exist(self):
        from snapshot import does_file_exist
        path = "/tmp/path/to/file"
        file_exists = does_file_exist(path)
        self.assertTrue(file_exists)
        path = "/tmp/file_doesnt_exist"
        file_doesnt_exists = does_file_exist(path)
        self.assertFales(file_doesnt_exists)