num=0
f = open(file="scores.txt",mode="r+",encoding="utf-8")
f2 = open(file="zongfen.txt",mode="w+",encoding="utf-8")
data = f.readlines()
for i in data:
    # print(i)
    da = i.replace("\n","").split(" ")
    print(da[0])
    f2.write(da[0])
    f2.write(" ")
    da1 = da
    del da1[0]
    # print(da1)
    for i in da1:
        # print(i)
        i = int(i)
        num = num +i

    # f2.write(str(num))
    # f2.write("\n")

f.close()
f2.close()