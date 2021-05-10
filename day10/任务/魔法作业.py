users = []
userss = []
f= open(file="scores.txt",mode="r+",encoding="utf-8")
f1= open(file="zongfen.txt",mode="w+",encoding="utf-8")
data = f.readlines()
# print(data)
s = 0
for i in data:
    da = i.replace("\n","").split(" ")
    users.append(da)
    # print(da[0])
    table = users[0+s][1:]
    s = s+1
    z = sum(list(map(int,table)))
    z= str(z)
    print(z)
    f1.write(da[0]+" "+z+"\n")
    # f1.write(" ")
    # f1.write(z)
    # f1.write("\n")
f1.close()
f.close()
