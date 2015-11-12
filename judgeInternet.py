#!/usr/bin/env python
#coding:utf-8
 
import os,subprocess
import requests
import time
import random
import time
import urllib
import urllib2

def netOkorFail():
    try: 
        is_online = u'<title>微软必应搜索' in urllib.urlopen("http://cn.bing.com").read().decode('utf-8')
    except BaseException, e:
        is_online=(2==1)
        fp=open('/home/pi/autologin_log.txt','a')
        ISOTIMEFORMAT='%Y-%m-%d %X'
        gettime=time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        fp.write(gettime)
        fp.write('\n')
        fp.write(str(e))
        fp.write('\n')
        fp.close()
    return is_online
def login():
    username = 'by1204122'
    password = 'c798de0148f6f192'
    payload ={'username':username,'password':password,'drop':'0','type':'1','n':'100'}
    url = "http://202.112.136.131/cgi-bin/do_login"
    res = requests.post(url, data = payload)
    #print response
    #print res.text
    fp=open('/home/pi/autologin_log.txt','a')
    ISOTIMEFORMAT='%Y-%m-%d %X'
    gettime=time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
    fp.write(gettime)
    fp.write('\n')
    fp.write(res.text)
    fp.write('\n')
    fp.close()
#i=1
while 1:
    #i=i+1
    time.sleep(random.uniform(20,40))
    if not netOkorFail():
        login()
        miao=random.uniform(30,80)
        time.sleep(miao)
    #print netOkorFail()    
    
