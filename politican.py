from db import DB

data=DB.execution("select * from area")   
for (areaid,name) in data:
    print(areaid,name.decode('utf-8'))