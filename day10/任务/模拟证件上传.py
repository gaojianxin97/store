s = input("请输入路径：")
f = open(file=s,mode="rb")
f1 =open(file="F:\Python自动化测试技术\Python\每天文件\day10\图片\呸.jpg",mode ="wb")

a = f.read()
f1.write(a)

f1.close()
f.close()



