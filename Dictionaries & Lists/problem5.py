import sys
import csv
import datetime

samplefile = open(sys.argv[1],"rb")

reader = csv.reader(samplefile)

counter = 0
DaysofWeek = {} #dictionary of weekdays (keys) and number of times they occured (values)

y = 0
x = 0

for row in reader:
    
    weekdays = 0 #created date in each row
    if y == 0: #check for first row (headers)
        y = y + 1 #start loop from row 2 (don't include header)
    else:
        x = x + 1 #check for second row (first row of data)
        weekdays = datetime.datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p').strftime('%A') #row[1] = open date. strptime is a function, needs to be in ()
    
        if weekdays in DaysofWeek.keys():#keys in a function, needs to be in ()
            DaysofWeek[weekdays]=DaysofWeek[weekdays]+1
        else:
            DaysofWeek[weekdays]=1

OrderofDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #list

for days in range(7): #range is a function between 0 and 7

    if OrderofDays[days] in DaysofWeek.keys(): #keys is a function and uses parenthesis 

        print OrderofDays[days], "==", DaysofWeek[OrderofDays[days]] #dictionary references use square brackets

    else:
        print OrderofDays[days], "==", 0 #set wording to match assignment

samplefile.close()
