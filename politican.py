from db import DB


def createlygov(data):
    # 搜尋選區
    areaName = data["areaName"]
    if(any(chr.isdigit() for chr in areaName)):
        num = ''.join([x for x in areaName if x.isdigit()])
        # print(num)
    sqlstr = "select * from area where name = \"%s\" " % areaName
    # print(sqlstr)
    # areaName = DB.execution(DB.select, sqlstr)
    # print(areaName)

    # 搜尋委員會
    sqlstr = "select * from committee where name = \"%s\" " % data["committee"]
    # print(sqlstr)
    # committee = DB.execution(DB.select, sqlstr)
    # print(committee)

    # 搜尋黨籍
    sqlstr = "select * from party where name = \"%s\" " % data["party"]
    print(sqlstr)
    party = DB.execution(DB.select, sqlstr)[0][0]

    sqlstr = ("insert into politician(term,name,sex,experience,tel,degree,address,partyid,photo) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"
              % (data["term"], data["name"], data["sex"],
                 data["experience"], data["tel"], data["degree"],
                 data["addr"], party, data["picUrl"]))
    print(sqlstr)
    DB.execution(DB.create, sqlstr)
