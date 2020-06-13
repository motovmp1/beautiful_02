import sys

from bs4 import BeautifulSoup as beau

soup = beau(open('/home/elsys/PycharmProjects/beautiful_01/bares.html'), "lxml")

filename = "bares.csv"
f = open(filename, "w")

headers = "ENDERECO, NUMERO, BARES\n"
f.write(headers)


for title in soup.findAll('div', {"class": "jet-listing-dynamic-field__inline-wrap"}):
    print(title.text + ",")
    f.write(title.text + "\n")

f.close()




