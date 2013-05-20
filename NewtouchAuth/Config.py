__author__ = 'YangKui'
#_*_encoding:utf-8_*_

import ConfigParser
import re
import os


class UserInfo:
    def __init__(self, name, cpuID, hddID, macID):
        self.data = "cpuID=" + cpuID + "&hddID=" + hddID + "&macID=" + macID

    def getData(self):
        return self.data


class Config:
    configFileName = "config.txt"

    def writeConfigFile(self):
        print 'No config file found !Ready create default config file'
        f = file(self.configFileName, 'w')
        text = ['[USER]',
                'name = 阳葵',
                'cpuID = 7cfa5e5c6559a281ceb2ee899278e722',
                'hddID = 3f536c8f802c21a209bd7f251c757c97',
                'macID = 167f9ad9992401fe068939058362712e%3B69226a927d029bb91de4f740182c0bf7%3B',
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



