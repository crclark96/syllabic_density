#!/usr/bin/python

import sys
from curses.ascii import isdigit
from nltk.corpus import cmudict

d = cmudict.dict()
def nsyl(word):
    try:
        return [len(list(y for y in x
                         if isdigit(str(y[-1]))))
                for x in d[word.lower()]]
    except KeyError:
        return [0]

if __name__ == '__main__':
    o = open('syllabic_density.txt','w')
    syllables = []
    for word in d.keys():
        syllables.append((word,nsyl(word)[0]))

    density = [(word,syllbs/float(len(word)))
               for word,syllbs in syllables
               if syllbs > 0]
    
    density.sort(cmp=lambda x,y: cmp(y[1],x[1]))
        
    for entry in density:
        o.write(entry[0] + ', ' + str(entry[1]) + '\r\n')

    

