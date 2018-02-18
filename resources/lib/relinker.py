import urllib
import urllib2
import urlparse

from .browser import Browser

class Relinker(Browser):
    def getURL(self, url):
        scheme, netloc, path, params, query, fragment = urlparse.urlparse(url)
        qs = urlparse.parse_qs(query)
    
        # output=20 url in body
        # output=23 HTTP 302 redirect
        # output=25 url and other parameters in body, space separated
        # output=44 XML (not well formatted) in body
        # output=47 json in body
        # pl=native,flash,silverlight
        # A stream will be returned depending on the UA (and pl parameter?)
        
        if "output" in qs:
            del(qs['output'])
        qs['output'] = "20"
        
        query = urllib.urlencode(qs, True)
        url = urlparse.urlunparse((scheme, netloc, path, params, query, fragment))
                
        response = urllib2.urlopen(url)
        mediaUrl = response.read().strip()
        
        # Workaround to normalize URL if the relinker doesn't
        mediaUrl = urllib.quote(mediaUrl, safe="%/:=&?~#+!$,;'@()*[]")
        
        return mediaUrl

