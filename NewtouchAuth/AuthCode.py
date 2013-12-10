__author__ = 'YangKui'

import cookielib
import urllib2


class AuthCode:
    cookieFileName = "local.txt"
    imageFilename = "code.jpg"

    def saveImage(self, url):
        mozillaCookieJar = cookielib.MozillaCookieJar(self.cookieFileName)
        mozillaCookieJar.save()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(mozillaCookieJar))
        urllib2.install_opener(self.opener)
        resp = self.opener.open(url)
        print 'mozillaCookieJar:', mozillaCookieJar
        mozillaCookieJar.save(self.cookieFileName, True, False)
        image = resp.read()
        print 'image read ok'
        with open(self.imageFilename, "wb") as jpg:
            jpg.write(image)
        print "image save success!"

    def loadCookie(self):
        parsedCookieJarFile = cookielib.MozillaCookieJar(self.cookieFileName)
        parsedCookieJarFile.load(self.cookieFileName, True, False)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(parsedCookieJarFile))
        urllib2.install_opener(self.opener)

    def kaoQin(self, postUrl, postData,host):
        print "doRequest url:", postUrl, "\n postData:", postData
        req = urllib2.Request(postUrl, postData)
        self.loadCookie()
        self.opener.addheaders = [('Host', host),
                                  ('User-Agent',
                                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C)'),
                                  ('Accept',
                                   'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*'),
                                  ('Accept-Language', 'zh-CN'),
                                  ('Accept-Encoding', 'gzip, deflate'),
                                  ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
                                  ('Connection', 'keep-alive'),
                                  ('Referer', 'http://'+host+'/attendance/record/record')]

        print 'starting request'
        response = self.opener.open(req)
        print 'end request'
        the_page = response.read()
        return the_page

    def __main__(self):
        authCode = AuthCode()
        authCode.saveImage("http://10.31.215.211:8080/attendance/jcaptcha/jpeg/imageCaptcha")

# authCode = AuthCode()
# authCode.saveImage("http://10.31.215.211:8080/attendance/jcaptcha/jpeg/imageCaptcha")
