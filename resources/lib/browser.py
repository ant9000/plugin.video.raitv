import urllib2

class Browser:
    # Rai.tv android app
    # UserAgent = "Apache-HttpClient/UNAVAILABLE (java 1.4)"
    # Firefox 29 on Android
    # UserAgent = "Mozilla/5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0"
    # Firefox 29 on Windows 7
    # UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0"
    # Firefox 29 on Linux
    # UserAgent = "Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0"
    # Raiplay android app
    # UserAgent = "Android 4.2.2 (smart) / RaiPlay 2.0.4 / WiFi"
    # Chrome 57 on Windows 10
    UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2956.0 Safari/537.36"

    def __init__(self):
        opener = urllib2.build_opener()
        # Set User-Agent
        opener.addheaders = [('User-Agent', self.UserAgent)]
        urllib2.install_opener(opener)
