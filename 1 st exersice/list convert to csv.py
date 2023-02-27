# list convert to csv file
import csv
heading=["Si.No","Name","Roll No","Class"]
values=[['1','selva','12345','10'],
        ['2','prakash','56789','10']]
with open('selva2.csv','w') as a:
    b=csv.writer(a)
    b.writerow(heading)
    b.writerows(values)