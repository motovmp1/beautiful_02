import sys

from bs4 import BeautifulSoup as beau

soup = beau(open('/home/elsys/PycharmProjects/beautiful_01/bares.html'), "html.parser")

filename = "bares.csv"
f = open(filename, "w")

# headers = "ENDERECO, NUMERO, BARES\n"
# f.write(headers)

#
# for title in soup.findAll('div', {"class": "jet-listing-dynamic-field__inline-wrap"}):
#     print(title.text + ",")


# for title in soup.findAll('div', {"class": "jet-listing jet-listing-dynamic-field display-inline"}):
# for title in soup.findAll('div', {"class": "jet-listing-dynamic-field__content"}):


nome_bar = soup.findAll('div', {"class": "elementor elementor-61"})
# print(len(nome_bar))
# print(nome_bar[3].text)

print(soup.prettify(nome_bar[0]))


# f.close()

