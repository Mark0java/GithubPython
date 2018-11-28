import io
import re
from xml.etree import ElementTree as et

"РІВЕНЬ 1:"
"Завдання №1"
f = open('text.txt')
count = 0
for line in f:
    print(line)
    count += 1

print("Кількість рядків = %d " % count)

"Завдання №2"
encoding = 'utf8'
fain = io.open('a.txt', 'r', encoding=encoding, newline='\n')
lines = fain.readlines()
fain.close()
fb1out = io.open('b1.txt', 'w', encoding=encoding, newline='\n')
fb2out = io.open('b2.txt', 'w', encoding=encoding, newline='\n')
for i in range(len(lines)):
    if (i % 2 == 0):
        fb1out.write(lines[i].upper())
    else:
        fb2out.write(lines[i].lower())
fb1out.close()
fb2out.close()
"РІВЕНЬ 2:"
"Завдання №2"
a = io.open('a.txt', 'r', encoding=encoding, newline='\n')
words = re.findall(r'[а-яієї’А-Я]*[а-яієї’А-Я]\b', a.read())
d = dict()
for i in words:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
import xml.etree.cElementTree as ET

root = ET.Element("root")
data = ET.SubElement(root, "data")
word = ET.SubElement(data, "word")
ends = re.findall(r'..\w\b', str(words))
print(ends)
e = dict()
for end in ends:
    if end not in e:
        e[end] = 1
    else:
        e[end] += 1
wordsinline = {}
k = 0
for line in lines:
    line = line.split()
    wordsinline[k] = len(line)
    k += 1
k = 0
wordit = 1
lineit = 0
for i in ends:
    word = ET.SubElement(data, "word")
    ET.SubElement(word, "word", name=str(words[k])).text = str(d[words[k]])
    ET.SubElement(word, "end", name=str(i)).text = str(e[i])
    ET.SubElement(word, "stringnumber").text = str(lineit + 1)
    ET.SubElement(word, "wordnumber").text = str(wordit)

    if wordit >= wordsinline[lineit]:
        lineit += 1
        wordit = 1
    else:
        wordit += 1
    k += 1

tree = ET.ElementTree(root)
tree.write("c.xml")