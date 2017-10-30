# coding=utf-8
# ref: http://blog.csdn.net/light_jiang2016/article/details/52474322
import os
class ConnectWeb(object):
    def __init__(self):
        # self.cookiejarinmemory = CookieJar()
        # self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookiejarinmemory))
        # urllib2.install_opener(self.opener)
        self.username = ""
        self.password = ""

    def disconnect(self):  # 断开wifi
        os.system("netsh wlan disconnect")

    def connect_wifi(self, name=None): #连接wifi
        os.system("netsh wlan connect name=%s" % name)

if __name__ == "__main__":
    test = ConnectWeb()
    test.connect_wifi('DIVI-2')