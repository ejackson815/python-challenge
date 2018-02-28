import csv

with open('budget_data_1.csv', mode = 'r') as infile:
    reader=csv.reader(infile)
    with open('newbudget_data_1.csv', mode = 'w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1]for rows in reader}
    print(mydict)
{k: sum(map(int, v)) for k, v in mydict.items()}

