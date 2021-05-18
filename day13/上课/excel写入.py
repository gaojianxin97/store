'''

'''
import  xlwt

# 空的工作簿
wb = xlwt.Workbook()

# 添加
sheet = wb.add_sheet("用户管理")


# 向选项卡里添加数据
sheet.write(0,0,"用户名")

# 保存
wb.save("用户管理.xls")



