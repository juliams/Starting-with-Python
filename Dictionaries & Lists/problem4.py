import sys
import csv
import operator

samplefile = open(sys.argv[1],"rb")
k = int(sys.argv[2]) #read second input in command line, k number of outputs

reader = csv.reader(samplefile)

y = 0
requiredcolumn = 0

counter = 0

for row in reader:
    for column in row:
        counter = counter + 1
        if column == "Complaint Type":
            requiredcolumn = counter -1

samplefile.close() #close file after identifying number of complaint typles


samplefile = open(sys.argv[1],"rb") #reopen

reader = csv.reader(samplefile)
ComplaintTypes = {} #this is an empty dictionary, stores keys & values

for row in reader: #start of the loop
    if y == 0:
        y = y + 1 #identify and exclude header
        continue
    else:
        if row[requiredcolumn] in ComplaintTypes.keys():
            ComplaintTypes[row[requiredcolumn]]+=1 #also can write as c = c + 1
        else:
            ComplaintTypes[row[requiredcolumn]]=1 #counts entries not previously identified

ComplaintTypes = sorted(ComplaintTypes.iteritems(), key=operator.itemgetter(0))
ComplaintTypes = sorted(ComplaintTypes, key=operator.itemgetter(1), reverse=True)

for i in xrange(k): #for variable in the range, run "k" times
    print ComplaintTypes[i][0], "with", ComplaintTypes[i][1], "complaints"

samplefile.close()