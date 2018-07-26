
import os
class FileEnd(Exception):
    pass

name = ['part1.txt', 'part2.txt', 'part3.txt', 'part4.txt']
nfile = r'C:\Users\wojci\Desktop\test\ICV.txt'
dir_name = os.path.dirname(nfile)
name=dir_name+'\part_{nr}.txt'

try:
    with open(nfile) as file:
        for i in range(0, 4):
            output = []
            for j in range(0, 100):
                # Split the current line into a list: line
                line = file.readline()
                output.append(line)
            with open(name.format(nr=i), 'w') as zapis:
                zapis.writelines(output)
            if line == '':
                raise FileEnd()
except FileEnd as e:
    print('File end')

# Print the resulting dictionary

