from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as soup

myurl = 'https://campinascomprelocal.com.br/tipo/bares/'
print(myurl)

# open connection page
uClient = UReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

nome_bar = page_soup.findAll('div', {"class": "elementor elementor-61"})
# print(len(nome_bar))
# print(nome_bar[3].text)

# print(soup.prettify(nome_bar[0]))

#
# descricao_bar = page_soup.findAll('div', {"class": "elementor-text-editor elementor-clearfix"})
# print(descricao_bar[0].text.strip())

filename = "bares.csv"
f = open(filename, "w")

headers = "ENDERECO, NUMERO, BARES\n"
f.write(headers)

for description in page_soup.findAll('div', {"class": "jet-listing-dynamic-field__content"}):
    final_desc = description.text
    print(final_desc.replace(",", "") + "," "\n")
    f.write(final_desc + "," + "\n")

f.close()
