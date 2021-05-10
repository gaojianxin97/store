f1 = open(file="F:\Python自动化测试技术\Python\每天文件\day10\代码\day10\呸.jpg",mode="rb")
f2 = open(file="F:\呸2.jpg",mode="wb")

data = f1.read()
f2.write(data)

f2.close()
f1.close()
