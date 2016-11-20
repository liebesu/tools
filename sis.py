import requests
from bs4 import BeautifulSoup
def login_page():
    
    login_url="http://174.127.195.202/bbs/logging.php?action=login"
    r=requests.Session()
    parms={'formhash':'5c0103b6',
    'referer':'',
    'cookietime':'2592000',
    'loginfield':'username',
    'username':'liushui52',
    'password':'liushui52',
    'questionid':'0',
    'answer':'',
    'loginsubmit':'true'}
    re=r.post(login_url,data=parms)
    frist_page(re.cookies)
def frist_page(lcookies):
    url="http://174.127.195.202/bbs/forum-213-1.html"
    new=requests.get(url,cookies=lcookies)
    
    print new.content
    soup=BeautifulSoup(new.content,"html5lib")    
def get_page_info(url,login_cookies):
    pass
def db_check():
    pass
    
if __name__=="__main__":
    login_page()
    