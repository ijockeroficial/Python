import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://google.com.br')
except urllib.error.URLError:
    print("ERRO!")
else:
    print("OK!")