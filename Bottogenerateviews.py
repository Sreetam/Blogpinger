import requests
import time
import sys
from torrequest import TorRequest
import numpy.random as nr
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #there will be warnings. but be sure to trust the website befor doing this
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

proxyPort=8080 #default tor config
ctrlPort=9051
site = ["https://sreetamspeaks.blogspot.com/2017/02/it-fascinates-me-to-read-about-lives-of.html",
        "https://sreetamspeaks.blogspot.com/2018/08/why-wont-you-just-sleep.html",
        "https://sreetamspeaks.blogspot.com/2018/08/twisted-meanings.html",
        "https://sreetamspeaks.blogspot.com/2018/08/its-farce.html",
        "https://sreetamspeaks.blogspot.com/2018/07/hi-welcome-back-to-my-blog.html",
        "https://sreetamspeaks.blogspot.com/2018/07/i-was-watching-conan-o-briens-interview.html",
        "https://sreetamspeaks.blogspot.com/2017/02/james-hogg-was-well-known-poet-but-he.html",
        "https://sreetamspeaks.blogspot.com/2017/02/sitting-alone-my-mind-oftenwanders-to.html",
        "https://sreetamspeaks.blogspot.com/2017/01/he-woke-up-in-this-morning-looked_19.html",
        "https://sreetamspeaks.blogspot.com/2017/01/thick-and-dark-clouds-sometimes.html"]  #use a longer list to avoid detection

blog = 3000000 # this is the number of times the website needs to be pinged

if __name__ == '__main__':
    if len(sys.argv) > 3:
        if sys.argv[1] and sys.argv[2]:
            proxyPort=sys.argv[1]
            ctrlPort=sys.argv[2]
    with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
        for i in range(blog):
            response = tr.get(site[nr.randint(0,10)], headers=headers,verify=False)
            print ("Blog View "+str(i)+" Added With IP:" +str(tr.get('http://ipecho.net/plain').content))
            #time.sleep(nr.randint(60,100))  #for avoiding detection
            tr.reset_identity()
