#!/usr/bin/env python

"""
2014-08-02 JGM Created.
"""

import datetime
import pprint
from gmail import Gmail

class UtIntfGmail(object):
    def __init__(self, username, password):
        self.init(username, password)
        pass
    
    def init(self, username, password):
        self.__api_Gmail = Gmail()
        self.__api_Gmail.login(username, password)
        pass
    
    def exClassMethod(self):
        pprint.pprint(self.__api_Twit.statuses.user_timeline(screen_name="changetip", count=1))
        return True 
    
def main():
    dictCreds = {'oauthToken':r'119071459-5aqC11gJr7dWM3CV7hIfBRafRbqP61H2re9FMJ5G', 'oauthSecret':r'lbEl0qGss9JufUdLmBAYmSTD8Y2yRxTPFPIjZxBseiRZX',
             'consumerToken':r'LqoiTNZ0jPlJcYINW16Q', 'consumerSecret':'nKV112bUdsDKy31F8zbfEvO7UZERwHMW1LvWlF66X5w'}
    ut_intf_twitter = UtIntfTwitter(dictCreds)
    bRet = ut_intf_twitter.exClassMethod()

if  __name__ == "__main__":
    main()

    

