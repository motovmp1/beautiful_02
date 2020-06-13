from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as beau

myurl = 'https://campinascomprelocal.com.br/tipo/bares/'
print(myurl)


# open connection page
uClient = UReq(myurl)
page_html = uClient.read()
uClient.close()

soup = beau(page_html, 'lxml')


contents = soup.title
print(contents)

