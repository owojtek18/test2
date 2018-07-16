import re
import numpy as np

str = r'Ala poszla doszko ly k.k dd f http://www.python.org gjgg cfhfgg'
pattern = r'\w{3}\.\w+'
r = re.compile(pattern)
m = r.search(str)
print(m.group())

pattern = r'(\d+).(\d*)'
r = re.compile(r"\d+\.\d*")
m = r.match('Hello world, ...') # brak dopasowania
m = r.match('jj 225.25') # dopasowanie
print(m)

pattern = r'(\b\d+.\d{2}\$)'
str = 'xfhfxhx 12.25$  12.25$ 342.79$ + 12.56$ 12.56$ + 12.54+ 12.1$'

m = re.findall(pattern,str)
print(m)

