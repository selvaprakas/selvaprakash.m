# print a column of given csv file
import csv
a=open('selva.csv','r')
b=csv.DictReader(a)
c=[]
for x in b:
    c.append(x["Name"])
print(c)
