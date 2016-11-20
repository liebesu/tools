import requests
from bs4 import BeautifulSoup
def frist_page():
    url="http://174.127.195.202/bbs/forum-213-1.html"
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
    new=r.get(url,cookies=re.cookies)

    print new.content
    soup=BeautifulSoup(new.content,"html5lib")
def get_info(url):
    pass
def db_check():
    pass
    
if __name__=="__main__":
    pass
    