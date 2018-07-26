# from glob import glob
# from os import rename
# for fname in glob(r'C:\Users\wojci\Desktop\test\oms*.000'):
#     rename(fname, fname.replace("1523", "1820"))

from mathematicians import simple_get
from bs4 import BeautifulSoup
raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(raw_html, 'html.parser')
for i, li in enumerate(html.select('li')):
    print(i, li.text)




