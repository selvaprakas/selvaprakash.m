#dic convet to json file
import json
a={"Si.No":"1",
       "Name":"Selvaprakash",
       "Qualification":"DAE"}
with open('selva3.json','w') as b:
    x=json.dump(a,b)