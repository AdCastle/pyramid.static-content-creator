import urllib2
import logging
log = logging.getLogger(__name__)


def url_load(url):
    """
        param url: Given URL
        return: content or logged error

    """
    try:
        return urllib2.urlopen(url,
                               timeout=1)
    except urllib2.URLError, e:
        log.info("There was an error reading from URL: n"
                 "\n%r" % (url, e))
    return None


def grab_content():
    """
    look up the HTML page and return its content
    """
