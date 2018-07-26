from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/"

r= requests.get(url)
text = r.text
soup = BeautifulSoup(text)
#print(soup.get_text())
print(soup.children)

#print(list(soup.children)[0:3])


'''
for link in soup.find_all('a'):
    print(link.get('href'))
'''

#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("https://pl.wikipedia.org/wiki/Klasyfikacja_medalowa_Zimowych_Igrzysk_Olimpijskich_2018")
text = page.text


soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#print(list(soup.children))
html = list(soup.children)[2]
#print(list(html.children))

soup = BeautifulSoup(page.content, 'html.parser')
table = list(soup.find_all('table'))[0].text
print(type(str(table)))
print(str(table)[0:20])


from lxml import etree
s = """<table>
  <tr><th>Event</th><th>Start Date</th><th>End Date</th></tr>
  <tr><td>a</td><td>b</td><td>c</td></tr>
  <tr><td>d</td><td>e</td><td>f</td></tr>
  <tr><td>g</td><td>h</td><td>i</td></tr>
</table>
"""
print(type(s))
table = etree.HTML(r.text).find("body/table")
print(table)
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]
    print (dict(zip(headers, values)))

