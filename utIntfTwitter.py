#!/usr/bin/env python

"""
2014-08-02 JGM Created.

NOTES:

https://pypi.python.org/pypi/twitter
"""

import datetime
import pprint
from twitter import *

class UtIntfTwitter(object):
    def __init__(self, dictCreds):
        self.init(dictCreds)
        pass
    
    def init(self, dictCreds):
        auth = OAuth(dictCreds['oauthToken'], dictCreds['oauthSecret'], dictCreds['consumerToken'], dictCreds['consumerSecret'])
        
        self.__api_Twit = Twitter(auth=auth)
        pass
    
    def exClassMethod(self):
        import json
        #pprint.pprint(self.__api_Twit.statuses.user_timeline(screen_name="changetip", count=1))
        for i in range(1):
            res = self.__api_Twit.search.tweets(q="#pycon")
            print json.dumps(res)
        return True 
    
def main():
    dictCreds = {'oauthToken':r'119071459-5aqC11gJr7dWM3CV7hIfBRafRbqP61H2re9FMJ5G', 'oauthSecret':r'lbEl0qGss9JufUdLmBAYmSTD8Y2yRxTPFPIjZxBseiRZX',
             'consumerToken':r'LqoiTNZ0jPlJcYINW16Q', 'consumerSecret':'nKV112bUdsDKy31F8zbfEvO7UZERwHMW1LvWlF66X5w'}
    ut_intf_twitter = UtIntfTwitter(dictCreds)
    bRet = ut_intf_twitter.exClassMethod()

if  __name__ == "__main__":
    main()

    

