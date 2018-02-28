import csv
import os

csvpath = os.path.join('budget_data_1.csv')

numlines = 0
total = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    line = csvfile.readline()
     #calculating data
    for row in csvreader:
        numlines += 1
        revenue = row[1]
        revenue += revenue
        date = numlines - 1
        line = csvfile.readline()
    average = float(revenue)/date
with open('budget_data_1.csv', mode = 'r') as infile:
    reader=csv.reader(infile)        
#creating dictionary    
    with open('newbudget_data_1.csv', mode = 'w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1]for rows in reader}
        #print(mydict)
rev_max = max(mydict.keys(), key=(lambda k: mydict[k]))
rev_min = min(mydict.keys(), key=(lambda k: mydict[k]))   

#Terminal Output
print("Number of Months: ", numlines - 1)
print("Total Revenue: $", revenue)
print("Average Revenue: $", average)
print("Max Revenue: $",mydict[rev_max], max(mydict))
print("Min Revenue: $",mydict[rev_min], min(mydict))


# variables for output file
months = "Number of Months: ", numlines - 1
Trev = "Number of Months: ", numlines - 1
Average_Rev = "Average Revenue: $", average
Max_val = "Max Revenue: $",mydict[rev_max], max(mydict)
Min_val = "Min Revenue: $",mydict[rev_min], min(mydict)

with open('newbudget_data_1.csv', mode = 'w') as outfile:
    writer = csv.writer(outfile)
    print("Number of Months: ".format(numlines - 1), file = outfile)
    print("Total Revenue: $" .format(revenue), file = outfile)
    print("Average Revenue: $" .format(average), file = outfile)
    print("Max Revenue: $".format(mydict[rev_max], max(mydict), file = outfile))
    print("Min Revenue: $".format(mydict[rev_min], min(mydict)),, file = outfile)
    outfile.close()





























