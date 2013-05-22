__author__ = 'YangKui'
#_*_encoding:utf-8_*_

import ConfigParser
import re
import os
import hashlib
import time


class UserInfo:
    def __init__(self, name, cpuID, hddID, macID1, macID2):
        t = time.strftime('%m-%d', time.localtime(time.time()))
        c = self.md5(cpuID)
        h = self.md5(hddID + t)
        m1 = self.md5(macID1 + t)
        m2 = self.md5(macID2 + t)
        self.data = "cpuID=" + c + "&hddID=" + h + "&macID=" + m1 + "%3B" + m2 + "%3B"

    def getData(self):
        return self.data

    def md5(self, string):
        return hashlib.md5(string).hexdigest().lower()


class Config:
    configFileName = "config.txt"

    def writeConfigFile(self):
        print 'No config file found !Ready create default config file'
        f = file(self.configFileName, 'w')
        text = ['[USER]',
                'name = 阳葵',
                'cpuID = BFEBFBFF000206A7',
                'hddID = 2085256266',
                'macID1 = F0:DE:F1:70:C5:64',
                'macID2 = 8C:A9:82:B7:7C:E6',
                '[URL]',
                'authCodeUrl = http://10.31.215.211:8080/attendance/jcaptcha/jpeg/imageCaptcha',
                'postUrl= http://10.31.215.211:8080/attendance/record/save']
        for x in text:
            f.write(x + "\n")
        f.close()
        print 'default config file write ok!'

    def __init__(self):
        print '####starting load config.txt####'
        if (not os.path.isfile(self.configFileName)):
            self.writeConfigFile()

        f = file(self.configFileName)

        ConfigParser.RawConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
        self.CONFIG = ConfigParser.ConfigParser()
        self.CONFIG.read(self.configFileName)
        self.USER = {}
        USERNAME = self.CONFIG.get('USER', 'name').split("|")
        CPUID = self.CONFIG.get('USER', 'cpuID').split("|")
        HDDID = self.CONFIG.get('USER', 'hddID').split("|")
        MACID1 = self.CONFIG.get('USER', 'macID1').split("|")
        MACID2 = self.CONFIG.get('USER', 'macID2').split("|")

        i = 0
        for key in USERNAME:
            userInfo = UserInfo(key, CPUID[i], HDDID[i], MACID1[i], MACID2[i])
            self.USER[key] = userInfo
            i = i + 1
        self.AUTHCODEURL = self.CONFIG.get('URL', 'authCodeUrl')
        self.POSTURL = self.CONFIG.get('URL', 'postUrl')

        for key, value in self.USER.items():
            print "USERNAME:", key, value.data

        # print self.USER['阳葵'].data

        print 'authCodeUrl:', self.AUTHCODEURL
        print 'postUrl:', self.POSTURL
        print '####end load config.txt####'

# config = Config()



