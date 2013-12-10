__author__ = 'YangKui'
#_*_encoding:utf-8_*_
import time
class LogFile:
    logFileName = "log.txt"
    def info(self,text):
        t = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time()))
        line = t+'-'+str(text)+'\n'
        print line
        file_object = open(self.logFileName, 'a')  #追加文件
        file_object.writelines(line)
        file_object.close()
