import xlrd

#获取工作簿
wb = xlrd.open_workbook(filename="F:\Pythonwenjian\day13\上课\学生表.xlsx",encoding_override=True)

#通过wb获取选项卡
sheet = wb.sheet_by_name("学生信息")

#获取行，列数据
rows = sheet.nrows #多少行
cols = sheet.ncols #多少列

for i in range(rows):
    for j in range(cols):
          print(sheet.cell_value(i,j))
    #     print(sheet.cell_value(i,j),end = "") #end = ""不换行
    # print()

# for i in range(rows):
#     print(sheet.row_values(i))