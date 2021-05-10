import pymysql
from DBUtils import update
from DBUtils import select
users=[]
f = open(file="用户数据.txt",mode="r+",encoding="utf-8")
a = f.readlines()
# print(a)
s = 0
for i in a:
     # replace("\n",""):将\n替换为空,  split(","):指定分隔符，进行切片
    da = i.replace("\n","").split(",")
    users.append(da)
    print(users[0+s][0],users[0+s][1],users[0+s][2])
    sql = "insert into yonghu value (%s,%s,%s)"
    param = [users[0+s][0],users[0+s][1],users[0+s][2]]
    update(sql,param)
    s = s+1

#资产求和
sql2 = "SELECT SUM(money)AS money FROM yonghu"
param2 = []
data = select(sql2,param2)
print("总资产：",data[0][0])

#  总资产插入数据库
w = "总资产："
sql1 = "INSERT INTO yonghu VALUE(%s,%s,%s)"
param1 = [w,"",data[0][0]]
data2 =update(sql1,param1)
f.close()
