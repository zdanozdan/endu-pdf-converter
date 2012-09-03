# This Python file uses the following encoding: utf-8

import xml.dom.minidom
import itertools
import csv

dom = xml.dom.minidom.parse('borowno.xml')

def getElement(line):
        if line.length:        
            l = line[0].childNodes
            if l:
                return getElement(l)
            else:
                return line[0].data
        else:
            return line[0].data
    
        

def getLine(dom):
    text = dom.getElementsByTagName('text')

    enduWriter = csv.writer(open('borowno.csv', 'wb'))

    c = itertools.cycle(range(1,18))
    l = []

    for count,data in zip(c,text):
        data = getElement(data.childNodes)
        l.append(data.encode('utf-8'))

        if count == 17:
            if l[13].startswith('K'):
                l.insert(16,'')            
            else:
                l.append('')            

            enduWriter.writerow(l)
            del l[:]
getLine(dom)

