__author__ = 'YangKui'
import urllib
import urllib2
import cookielib

class Login:
    loginURL = "http://eds.newtouch.cn/edsmanager/login.aspx"
    def login(self,openner,userId,password):
        print "do loging"
        data = 'UserId='+userId+"&UserPsd="+password
        req = urllib2.Request(self.loginURL, data)
        req.addheaders = [('Host', 'eds.newtouch.cn'),
                       ('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER'),
                       ('Accept', 'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*'),
                       ('Accept-Language', 'zh-CN'),
                       ('Accept-Encoding', 'gzip, deflate'),
                       ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
                       ('Connection', 'keep-alive'),
                       ('Referer', 'http://eds.newtouch.cn/edsmanager/login.html')]
        response = urllib2.urlopen(req)
        print response.read()
    def __main__(self):
        login =  Login()
        # cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(opener)
        login.login(opener,'09101','amcucn789')

login =  Login()
# cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(opener)
login.login(opener,'09101','amcucn789')


