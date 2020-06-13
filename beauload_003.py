import sys

from bs4 import BeautifulSoup as beau

soup = beau(open('/home/elsys/PycharmProjects/beautiful_01/bares.html'), "lxml")

filename = "bares.csv"
f = open(filename, "w")

# headers = "ENDERECO, NUMERO, BARES\n"
# f.write(headers)

#
# for title in soup.findAll('div', {"class": "jet-listing-dynamic-field__inline-wrap"}):
#     print(title.text + ",")

for text in soup.findAll('div', {"class": "elementor-text-editor elementor-clearfix"}):
    if len(text.text) > 0:
        final = (text.text.replace(",", "") + "," + "\n")
        print(final)
    else:
        text.text = ("falha")
        print(text.text)
    f.write(text.text.replace(",", "") + "," + "\n")


f.close()
