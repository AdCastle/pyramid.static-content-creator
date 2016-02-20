import urllib2
import logging
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

def diff_content(url, page):
    