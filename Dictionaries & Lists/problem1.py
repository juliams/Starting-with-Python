import sys
import csv
import datetime

samplefile = open(sys.argv[1],"rb")

reader = csv.reader(samplefile)

x = 0 #establish x and y to start loop
y = 0

first = 0 #earliest date
last = 0 #latest date

for row in reader:
    #for column in row:
        #if column == "created date":
            #print "yes"

    t = 0 #created date in each row
    if y == 0: #check for first row (headers). "==" for comparison, "=" for assignment
        y = y + 1 #start loop from row 2 (don't include header)
    else:
        x = x + 1 #check for second row (first row of data)
        t = datetime.datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p') #row[1] = open date

        if x == 1: #created date in each row
            first = t #set current t as first and last values
            last = t
        else: #loop to establish order of dates
            if t < first:
                first = t #set lowest numbers as first until end of loop
            if t > last: 
                last = t #set highest numbers as last until end of loop

first = first.strftime('%m/%d/%Y %H:%M:%S') #format date and time
last = last.strftime('%m/%d/%Y %H:%M:%S')

print x, "complaints between", first, "and", last #update wording to match assignment

samplefile.close()