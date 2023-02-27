# print in values only
import csv
a=open('selva.csv','r')
b=csv.reader(a)
c=list(b)
print(c)

#print in key with value
x=open('selva.csv','r')
y=csv.DictReader(x)
for z in y:
    print(z)