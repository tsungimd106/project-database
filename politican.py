from db import DB

data=DB.execution("select * from area")   
for (areaid,name) in data:
    print(areaid,str(name,'utf-8'))