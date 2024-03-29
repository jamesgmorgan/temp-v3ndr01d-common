#!/usr/bin/env python

"""
2014-08-02 JGM Created.

NOTES:

Wraps: https://pypi.python.org/pypi/twitter (docs: https://dev.twitter.com/docs/api/1.1)

Handy: http://www.jsoneditoronline.org
Investigate: https://github.com/vinta/awesome-python
Do: http://stackoverflow.com/questions/2397822/what-is-the-best-practice-for-dealing-with-passwords-in-github
"""

import datetime
import json
import pprint
from twitter import *

class UtIntfTwitter(object):
    def __init__(self, dictCreds):
        self.init(dictCreds)
        pass
    
    def init(self, dictCreds):
        if not dictCreds:
            try:
                jsonFile = __file__ + ".json"
                dictCredsJson = open(jsonFile, 'r').read()
                dictCreds = json.loads(dictCredsJson)
            except:
                raise
            
        auth = OAuth(dictCreds['oauthToken'], dictCreds['oauthSecret'], dictCreds['consumerToken'], dictCreds['consumerSecret'])
        
        self.__api_Twit = Twitter(auth=auth)
        pass
    
    def exClassMethod(self):
        import json
        #pprint.pprint(self.__api_Twit.statuses.user_timeline(screen_name="changetip", count=1))
        for i in range(1):
            res = self.__api_Twit.search.tweets(q="#payitforward", result_type="recent")
            statuses = res['statuses']
            for stat in statuses:
                created = stat['created_at']
                user = stat['user']['screen_name']
                text = stat['text'].encode('unicode-escape')
                line = "%s %s %s" % (created, user, text)
                print line
        return True

    def followers(self):
        def process(scr_names):
            res = self.__api_Twit.users.lookup(screen_name=','.join(scr_names), _timeout=1)
            for item in res:
                loc = item['location'].lower()
                if "dominica" in loc:
                    print "%-20s %-30s %s" % (item['screen_name'], item['location'], item['description'])
                    #import pprint
                    #pprint.pprint(item)

        import json
        #pprint.pprint(self.__api_Twit.statuses.user_timeline(screen_name="changetip", count=1))
        with open(r'C:\Dropbox\Proj\GitHub\v3ndr01d\followers.txt') as f:
            scrname_list = f.read().splitlines()
        n_total = len(scrname_list)
        n_hundreds = n_total/100
        for i in range(0, n_hundreds):
            r_lower = i*100
            r_upper = r_lower + 99
            #print "%d" % (r_upper)
            sub_list = scrname_list[r_lower:r_upper]
            process(sub_list)
        r_lower = n_hundreds*100
        r_upper = r_lower + n_total - r_lower
        sub_list = scrname_list[r_lower:r_upper]
        process(sub_list)


def main():
    ut_intf_twitter = UtIntfTwitter(None)
    bRet = ut_intf_twitter.followers()

if __name__ == "__main__":
    main()
