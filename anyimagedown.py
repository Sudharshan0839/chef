import random
import urllib.request

def img(url):
    name = str(random.randrange(0,100)) + ".mkv"
    urllib.request.retrive(url,name)

img(input())
