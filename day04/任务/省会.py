# 将中国所有省会城市添加到上述列表中
'''
city = [(' 合肥 ' , ' 北京 ' , ' 重庆 ' , ' 福州 ' , ' 兰州 ' , ' 广州 ' , ' 南宁 ' ,
        ' 贵阳 ' , ' 海口 ' , ' 石家庄 ' , ' 哈尔滨 ' , ' 郑州 ' , ' 香港 ' , ' 武汉 ' ,
        ' 长沙 ' , ' 南京 ' , ' 南昌 ' , ' 长春 ' , ' 沈阳 ' , ' 澳门 ' , ' 呼和浩特 ' ,
        ' 银川 ' , ' 西宁 ' , ' 济南 ' , ' 上海 ' , ' 太原 ' , ' 西安 ' , ' 成都 ' ,
        ' 台北 ' , ' 天津 ' , ' 乌鲁木齐 ' , ' 拉萨 ' , ' 昆明 ' , ' 杭州 ' )]


# 广东成为第二大发达城市，将广东排在上海前面

A = ["北京","上海","广东"]
A.remove("广东")
A.insert(1,"广东")
print(A)
'''

# 前8城市的GDP总和，平均GDP
B = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
C = sum(B)
D =(sum(B))/len(B)
D= round(D,2)
print("GDP总和为：",C)
print("平均GDP为：",D)