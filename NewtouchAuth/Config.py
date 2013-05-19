__author__ = 'YangKui'
#_*_encoding:utf-8_*_

import ConfigParser
import re


class UserInfo:
    def __init__(self, name, cpuID, hddID, macID):
        self.data = "cpuID=" + cpuID + "&hddID=" + hddID + "&macID=" + macID

    def getData(self):
        return self.data


class Config:
    configFileName = "config.txt"

    def __init__(self):
        print '####starting load config.txt####'
        f = file(self.configFileName)
        ConfigParser.RawConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
        self.CONFIG = ConfigParser.ConfigParser()
        self.CONFIG.read(self.configFileName)
        self.USER = {}
        USERNAME = self.CONFIG.get('USER', 'name').split("|")
        CPUID = self.CONFIG.get('USER', 'cpuID').split("|")
        HDDID = self.CONFIG.get('USER', 'hddID').split("|")
        MACID = self.CONFIG.get('USER', 'macID').split("|")
        i = 0
        for key in USERNAME:
            userInfo = UserInfo(key, CPUID[i], HDDID[i], MACID[i])
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



