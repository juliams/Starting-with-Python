import sys
import csv
import operator

samplefile = open(sys.argv[1],"rb")

reader = csv.reader(samplefile)

y = 0
requiredcolumn = 0

counter = 0

for row in reader:
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

ComplaintTypes = sorted(ComplaintTypes.iteritems(), key=operator.itemgetter(0)) # sort alphabetically
ComplaintTypes = sorted(ComplaintTypes, key=operator.itemgetter(1), reverse=True) #sort by decreasing number of complaints 

for keys, values in ComplaintTypes:
    print keys, "with", values, "complaints"

samplefile.close()