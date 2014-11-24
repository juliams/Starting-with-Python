import sys
import csv
import operator
from collections import defaultdict
from collections import Counter

samplefile = open(sys.argv[1],"rb")

reader = csv.reader(samplefile)

d = defaultdict(list)

counter = 0

Complaints = {} #dictionary of agencies (keys) and zip codes from which complaints originated (values)

y = 0
x = 0

for row in reader:
    
    agencies = 0 #created date in each row
    if y == 0: #check for first row (headers)
        y = y + 1 #start loop from row 2 (don't include header)
    else:
        x = x + 1 #check for second row (first row of data)

        d[row[3]].append(row[7])

alphaagencies = [] #list of agencies in alphabetical order

for agencynames in d.keys():
    alphaagencies.append(agencynames)
alphaagencies.sort() #function

for agencynames in alphaagencies: #this is a list, not a function (no parenthesis)
    agencylists = Counter(d[agencynames]).most_common()

    print agencynames, #comma, print doesn't move on to next line
    for item in agencylists: #counts across agencylists
        print item[0], #print zip code (first item in list)
    print item[1] #print complaints

#row[3] = agency name
#agencies = key
#all zip codes = values