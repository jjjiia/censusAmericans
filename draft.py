import csv     
#all headers
#def dataHeaders():
#    with open('alabama.csv', 'rb') as csvfile:
#        spamreader = csv.reader(csvfile)
#        for row in spamreader:
#            return row
#            
#headers in current data    
#headers_long = ["ST","CIT","CITWP05","CITWP12","COW","DEAR","DEYE","DOUT","DPHY","DREM","ENG","FER","GCL","GCM","GCR","HINS1","HINS2","HINS3","HINS4","HINS5","HINS7","JWMNP","JWRIP","JWTR","LANX","MAR","MARHD","MARHM","MARHT","MARHW","MARHYP05","MARHYP05","MIG","MIL","MLPA","MLPB","MLPCD","MLPE","MLPH","MLPJ","NWLA","NWLK","OIP","PAP","RELP","RETP","SCH","SCHG","SCHL","SEMP","SEX","WKHP","WKL","WKW","YOEP05","YOEP12","ANC","ANC1P05","ANC1P12","ESP","FOD1P","FOD2P","HICOV","INDP","JWAP","JWDP","LANP05","MSP"]
headers = ["JWMNP","CITWP05","MARHYP05","WKHP","WAGP","JWDP","ANC","ST","ANC1P12","FER","JWAP","MARHT","NWLA","CIT","FOD1P","JWRIP","MARHW","NWLK","COW","GCL","JWTR","MIG","SCHL","DEAR","GCM","LANP05","DEYE","HICOV","MAR","MIL","VPS","ENG","HISP","MARHD","NATIVITY","WAOB","ESP","INDP","MARHM","NOP","WKW"]
def dataHeaders():
    with open('alabama.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            return row

#get headers in use index in all headers
def getHeaderIndex():
    headerDictionary = {}
    indexList = []
    for header in headers:
        #print header
        headerIndex = dataHeaders().index(header)
        headerDictionary[header]=headerIndex
        indexList.append(headerIndex)
    #return headerDictionary
    return indexList

def reduceDataByColumn(infile,outfile):
    print "reduce to useful columns ..."
    indexList = getHeaderIndex()
    reducedRowsList = []
    with open(outfile,'wb') as outputFile:
        spamwriter = csv.writer(outputFile)
        with open(infile, 'rb') as csvfile:
            spamreader = csv.reader(csvfile)
           # headerDictionary = replaceHeaderCodes()
            rowsDone = 0
            for row in spamreader:
                reducedRow = []
                for index in indexList:
                    reducedRow.append(row[index])
                if reducedRow in reducedRowsList:
                    print "dupilicat"
                else:
                    spamwriter.writerow(reducedRow)
    #            print reducedRow

def columnDicts(infile):
    with open(infile, 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        headers = spamreader.next()
        #print headers
        outfile = {}
        for row in spamreader:
            outfile[row[0]]=row[1]
        return outfile


def fillInData(infile,outfile):
    print "filling in data ..."
    rowsDone = 0
    with open(outfile,'wb') as outputfile:
        w = csv.writer(outputfile)
        with open(infile,'rb') as datafile:
            r = csv.reader(datafile)
            headers = r.next()
            print headers
            #print currentIndex
            for row in r:
                rowsDone +=1
                if rowsDone%10000==0:
                    print rowsDone
                for i in headers:
                    currentIndex = headers.index(i)
                    currentDictionary = columnDicts("category_dictionaries/"+i+'.csv')
                    if row[currentIndex] in currentDictionary:
                        if i == "ST":
                            state = currentDictionary[row[currentIndex]]
                            greeting = "hi from "+state+","
                            row[0]=greeting
                            row[currentIndex]=""
                        else:
                            row[currentIndex]=currentDictionary[row[currentIndex]]
                    elif i == "CITWP05":
                        if row[currentIndex]!="" and row[currentIndex]!="-009" and len(row[currentIndex])==4:
                            #print row[currentIndex]
                            row[currentIndex] = "I was naturalized in " + str(row[currentIndex])+". "
                            #print row[currentIndex]
                        else:
                            row[currentIndex] =""
                    elif i == "JWMNP":
                        if [row[currentIndex]][0] !="":
                            commute = int([row[currentIndex]][0])
                            if commute < 11:
                               row[currentIndex] = "it only takes me "+str(commute)+"mins to get to work."
                            elif commute >10:
                               row[currentIndex] = "my daily commute is "+str(commute)+"mins long"                                
                            elif commute >120:
                               row[currentIndex] = "It takes me more than 2 hours to get to work. "
                            else:
                                row[currentIndex] = ""                            
                        else:
                            row[currentIndex] = ""
                        
                    elif i == "MARHYP05":
                        #check times married
                        timesMarried = row[headers.index("MARHT")]
                        if timesMarried == "1" or timesMarried == "I have only been married once. ":
                            phrase = "I got married in "
                            row[currentIndex] = phrase+row[currentIndex]+". "
                        else:
                            if row[currentIndex] !="" and row[currentIndex]!= " " and len(row[currentIndex])==4:
                                 phrase = "Last time I got married was in "
                                 row[currentIndex] = phrase+row[currentIndex]+". "
                            else:
                                row[currentIndex] = ""
                        #print row[currentIndex], row[headers.index("MARHT")]
                    elif i == "WKHP":
                        if row[currentIndex]!="":
                            hoursWorkedPerWeek = int([row[currentIndex]][0])
                            if hoursWorkedPerWeek > 40:
                                row[currentIndex] = "Usually work "+str(hoursWorkedPerWeek)+"hrs per week. "
                            else:
                                row[currentIndex] = "I work less than 40 hours per week. "
                        else:
                            row[currentIndex] =""
                
                w.writerow(row)
                
states = ['ak','usa','usb','usc','usd']
fileRoot = 'data/ss13p'
for i in range(len(states)):
    print i
    infile = fileRoot+states[i]+".csv"
    outfile = fileRoot+states[i]+"_out.csv"
    outfile2 = fileRoot+states[i]+"_filledin.csv"
    print infile,outfile,outfile2
    reduceDataByColumn(infile,outfile)
    fillInData(outfile,outfile2)