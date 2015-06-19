import csv
import random

def removeDups():
    with open("data/tweets.csv",'rb') as csvfile:
        spamreader = csv.reader(csvfile)
       # headerDictionary = replaceHeaderCodes()
        text = []
        dups = []
        for row in spamreader:
            #print row
            if row in text or len(row)>140:
                dups.append(row)
            else:
                text.append(row)
        print text
        print len(dups)
removeDups()
