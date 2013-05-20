__author__ = 'YangKui'

import re


def parseMessage(html):
    found = re.search('<div\s+?class="message">(?P<message>.+?)</div>', html)
    if (found):
        message = found.group("message")
        return message
    return "None"

    # f = open("test.html")
    # html = ""
    # while True:
    #     l = f.readline()
    #     print l
    #     if len(l)==0:
    #         break
    #     html +=l
    # message = parseMessage(html)
    # print message