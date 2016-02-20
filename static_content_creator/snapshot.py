import urllib2
import logging
import os.path

log = logging.getLogger(__name__)


def url_load(url):
    """
    :param url: Given URL
    :return: url object or logged error
    """
    try:
        return urllib2.urlopen(url,
                               timeout=10)
    except urllib2.URLError, e:
        log.info("There was an error reading from URL: %s"
                 "\n%r" % (url, e))
    return None


def check_code(page):
    """
    :param: urllib2 object is passed
    :return: checked code of page if it is a valid response
    then we return a true value
    """
    code = page.getcode()
    if (code >= 200 <= 206) or (code >= 300 <= 307):
        return code
    return None


def grab_content(url):
    """
    look up the HTML page and return its content
    :param url: Given URL
    :return: HTML content of page
    """
    load_content = url_load(url)
    if not load_content:
        return None
    if not check_code(load_content):
        return None
    return load_content.read()


def does_file_exist(path):
    """
    :param path: location of file
    """
    return os.path.exists(path)


def remove_domain_from_url(domain, url):
    if domain in url:
        url_with_domain_removed = url.split(domain)
        if len(url_with_domain_removed) > 1:
            return url_with_domain_removed[1]
    return None


def split_url_to_path(url):
    """
    :param: url
    :return: a path of the given url
    """
    if '/' in url:
        url = url.rstrip('/')
        path = url.split('/')
        return path
    return None


def save_content(url, page):
    """
    :param url: url of page
    :param page: content/HTML
    :return: save content to disk
    """
    return None


def read_content(url, page):
    """
    :param url: url of page
    :param page: content/HTML
    :return: read content from disk
    """
    return None


def diff_content(url, page):
    """
    :param url: url of page
    :param page: content/HTML
    :return: read content from disk
    """
    return None