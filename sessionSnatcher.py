import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

AMOUNT = 10000
REDDIT = 'https://reddit.com'

def getSession(lst):
    for dct in lst:
        if dct['name'] == 'session_tracker':
            return dct['value']


with open('sessions.txt','a') as s:
    for i in range(1,AMOUNT):
        try:
            ff = webdriver.Firefox()
            try:
                ff.set_page_load_timeout(3)
                ff.get(REDDIT)
            except Exception:
                ActionChains(ff).send_keys(Keys.ESCAPE)
        
            session_cookie = getSession(ff.get_cookies())
            if session_cookie != None:
                s.write(session_cookie + '\n')
                print('Writing session cookie number ' + str(i) + ': ' + session_cookie[0:8] + '...')
            ff.quit()
        except Exception:
            pass
