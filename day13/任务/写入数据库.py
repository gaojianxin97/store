import xlrd
import pymysql
print("开始了")
db = pymysql.connect(host="localhost",user="root",password="",database="销售数据库",charset='utf8')
cur = db.cursor()
ex = xlrd.open_workbook("F:/Python自动化测试技术/Python/每天文件/day13/任务/12月份衣服销售数据.xlsx")
sheet = ex.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols
# 跳过第一行的标题，直接从第二行真实数据开始
for i in range(1, rows):
    r=sheet.row_values(i)
    print(r)
    sql = "insert into xiaoshou VALUES (%s,%s,%s,%s,%s)"
    cur.execute(sql,r)
    db.commit()
cur.close()
db.close()
print("结束了")
