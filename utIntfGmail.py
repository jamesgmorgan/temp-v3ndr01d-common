#!/usr/bin/env python

"""
2014-08-02 JGM Created.
"""

import datetime
import pprint
from gmail import Gmail

class UtIntfGmail(object):
    def __init__(self, dictCreds):
        self.init(dictCreds)
        pass
    
    def init(self, dictCreds):
        self.__api_Gmail = Gmail()
        self.__api_Gmail.login(dictCreds['username'], dictCreds['password'])
        pass
    
    def getEmails(self, user):
        bRet = True
        bodyList = []
        mailList = self.__api_Gmail.inbox().mail(unread=True, sender=user)
        for m in mailList:
            m.fetch()
            bodyList.append(m.body)
        
        return bRet, bodyList
    
def main():
    dictCreds = {'username':r'v3ndr01d', 'password':r'6@OwA7wMB42BF^K&qLgC'}
    ut_intf_gmail = UtIntfGmail(dictCreds)
    bRet, bodyList = ut_intf_gmail.getEmails("support@changetip.com")
    pass

if  __name__ == "__main__":
    main()

    

