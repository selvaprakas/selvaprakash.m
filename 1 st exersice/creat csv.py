import csv
with open('selva.csv','w') as s:
    a=csv.writer(s)
    a.writerow(["Si.No","Name","Age","Qualification"])
    b=int(input("Enter the value of addenters"))
    for i in range(b):
        Si_No=int(input("eneter your number"))
        Name=input("enter name")
        Age=int(input("Enter age"))
        Qualification=input("Enter qualification")
        a.writerow([Si_No,Name,Age,Qualification])



