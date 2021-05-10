'''
    存储数据：
        1.变量
        2.元组，列表，字典，集合
        3.数据库：mysql   （pymysql）
        4.文件读写.txt
    1.打开文件
        模式：
        r、w、b（图片、mp3、mp4）、a（附加）、+可读可写
    2.写入数据
    3.关闭资源
'''

# 打开 ： 句柄 ， 把柄
f = open(file="古诗.txt", mode ="r+", encoding="utf-8")

# 写个数据
f.write("咏鹅\n")
f.write("【骆宾王】\n")
f.write("鹅鹅鹅，曲项向天歌。\n")
f.write("白毛浮丽水，\n")
f.write("红掌拨清波。\n")


#   print（f.read（））   #禁止使用
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

#  关闭资源
f.close()

