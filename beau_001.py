from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as beau

myurl = 'https://campinascomprelocal.com.br/tipo/alimentacao/'
print(myurl)


# open connection page
uClient = UReq(myurl)
page_html = uClient.read()
uClient.close()

soup = beau(page_html, 'lxml')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.text)

#print(soup.findAll('a'))

# for link in soup.findAll('a'):
#     print(link.get('href'))
#
# link_with_text = []
# for link in soup.findAll('a', href=True):
#     if link.text:
#         link_with_text.append(link['href'])
# print(link_with_text)
#
#
# for link in soup.findAll('a', href=True):
#     print(link['href'])





