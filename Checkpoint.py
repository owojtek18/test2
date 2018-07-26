import os
import re
class FileEnd(Exception):
    pass

nfile = r'C:\Users\olwo7001\Desktop\test\Week 28\ALL1001FDK.CHK'
dir_name = os.path.dirname(nfile)
name=dir_name+'\part_{nr}.txt'

f = open(nfile,'r')


with open(nfile,'r') as f:
    for x in f:
        x = x.rstrip()
        if x[0:7] =='Check2 ':
            cos = x
            while cos:
                cos = f.readline()
                print(re.sub(' +', ' ', cos))
                if cos[0] == '_':
                    break
