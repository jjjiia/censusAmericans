import csv
import random
states = ['ak','usb','usc','usd']
currentFile = 0
fileRoot = 'data/ss13p'
priority1 = []
priority2 = []
priority3 = []
def reduceDataByColumn(infile,outfile):
    existingTweets = []
    with open(outfile,'wb') as outputFile:
        spamwriter = csv.writer(outputFile)
        with open(infile, 'rb') as csvfile:
            spamreader = csv.reader(csvfile)
           # headerDictionary = replaceHeaderCodes()
            for row in spamreader:
                newRow = []
                newRowText = ""
                for column in row:
                    if len(column)>6:
                        newRow.append(column)
                        newRowText+=column
                shortTweet = ""
                rowLength = len(newRow)
                sampling = random.sample(range(1, len(newRow)), rowLength-1)
                for i in sampling:
                    shortTweet += str(newRow[i])
                
                while len(newRowText) > 140 and rowLength > 3:
                    sampling = random.sample(range(1, len(newRow)), rowLength-1)
                    rowLength = rowLength-1
                    #print sampling
                    shortTweet = ""
                    for i in sampling:
                        shortTweet += str(newRow[i])
                    #print len(shortTweet)
                #print newLine
                    #print shortTweet
                if shortTweet in existingTweets:
                    print "repeat"
                else:
                    spamwriter.writerow([shortTweet])
                
infile = fileRoot+states[currentFile]+"_filledin.csv"
outfile = fileRoot+states[currentFile]+"_refined.csv"
reduceDataByColumn(infile,outfile)

maxLength = 31
def findCompleteRow(infile):
    maxLength = 0
    with open(infile, 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
       # headerDictionary = replaceHeaderCodes()
        for row in spamreader:
            rowLength = len(row)
            for column in row:
                if column == "":
                    rowLength = rowLength-1
            if rowLength > 30:
                print row
        print maxLength
                
#findCompleteRow(infile)