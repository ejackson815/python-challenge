import csv

# open the file in universal line ending mode 
with open('budget_data_1.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

# Storing Date & Revenue values
date = data['Date']
revenue = data['Revenue']
TotalRevenue = 0
#calculations   
print(max(revenue))
print(min(revenue))





