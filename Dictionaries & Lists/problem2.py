import sys
import csv
import operator

samplefile = open(sys.argv[1],"rb")

reader = csv.reader(samplefile)

y = 0
requiredcolumn = 0

counter = 0

for row in reader: #shows column in which "Complaint Type" is located
    for column in row:
        counter = counter + 1
        if column == "Complaint Type":
            requiredcolumn = counter -1

samplefile.close()


samplefile = open(sys.argv[1],"rb")

reader = csv.reader(samplefile)
ComplaintTypes = {} #this is an empty dictionary, stores keys & values

for row in reader: #start of the loop
    if y == 0:
        y = y + 1
        continue
    else:
        if row[requiredcolumn] in ComplaintTypes.keys():
            ComplaintTypes[row[requiredcolumn]]+=1 #also can write as a = a + 1
        else:
            ComplaintTypes[row[requiredcolumn]]=1 #counts entries not previously identified

for keys, values in ComplaintTypes.iteritems(): 
    print keys, "with", values, "complaints"

samplefile.close()