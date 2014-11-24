import sys
import csv
import operator

samplefile = open(sys.argv[2],"rb")

reader = csv.reader(samplefile)

y = 0
requiredcolumn = 0

counter = 0

reader = csv.reader(samplefile)
Boroughs = {} #this is an empty dictionary, stores keys & values

for row in reader: #start of the loop
    if y == 0:
        y = y + 1 #identify and exclude header
        continue
    else:
        Boroughs[row[0]]=row[1] #row 0 contains zip, row 1 contains borough

samplefile.close()

samplefile = open(sys.argv[1],"rb")

reader = csv.reader(samplefile)

zipfinder = {}
y = 0
for row in reader: #start of the loop
    if y == 0:
        y = y + 1
        continue
    else:
        if Boroughs[row[7]] in zipfinder.keys():
            zipfinder[Boroughs[row[7]]]+=1
        else:
            zipfinder[Boroughs[row[7]]]=1

zipfinder = sorted(zipfinder.iteritems(), key=operator.itemgetter(1), reverse=True)

for keys, values in zipfinder: #remove iteritems once converted to a list
    print keys, "with", values, "complaints"

samplefile.close()