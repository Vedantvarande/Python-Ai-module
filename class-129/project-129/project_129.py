import csv
import pandas as pd

data_file1 = 'Unit converted Stars.csv'
data_file2 = 'Bright Stars.csv'

data1 = []
data2 = []

with open(data_file1, 'r') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        data2.append(i)
        
with open(data_file2, 'r') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        data1.append(i)

h1 = data1[0]
h2 = data2[0]

p_d1 = data1[1:]
p_d2 = data2[1:]

h = h1+h2

p_d =[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
with open("Total_Stars.csv", 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)