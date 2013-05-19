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
        print 'save cookie success!'
        image = resp.read()
        with open(self.imageFilename, "wb") as jpg:
            jpg.write(image)
        print "image save success!"

    def loadCookie(self):
        parsedCookieJarFile = cookielib.MozillaCookieJar(self.cookieFileName)
        parsedCookieJarFile.load(self.cookieFileName, True, False)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(parsedCookieJarFile))
        urllib2.install_opener(self.opener)

    def kaoQin(self, authCode):
        self.url = 'http://10.31.215.211:8080/attendance/record/save'
        self.postData = 'captcha=' + authCode + '&cpuID=7cfa5e5c6559a281ceb2ee899278e722&hddID=a4a651abf73599c037d429e289620875&' \
                                                'macID=92c29457a7fd80f0c5a5a284a221f47b%3B184f8ce29a433e23501b10b355d837f1%3B'
        req = urllib2.Request(self.url, self.postData)
        self.loadCookie()
        self.opener.addheaders = [('Host', '10.31.215.211:8080'),
                                  ('User-Agent',
                                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C)'),
                                  ('Accept',
                                   'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*'),
                                  ('Accept-Language', 'zh-CN'),
                                  ('Accept-Encoding', 'gzip, deflate'),
                                  ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
                                  ('Connection', 'keep-alive'),
                                  ('Referer', 'http://10.31.215.211:8080/attendance/record/record')]

        print 'starting request'
        response = self.opener.open(req)
        print 'end request'
        the_page = response.read()
        print the_page

    def __main__(self):
        authCode = AuthCode()
        authCode.saveImage("http://captcha.qq.com/getimage?aid=1007901&r=0.4029927267692983")


