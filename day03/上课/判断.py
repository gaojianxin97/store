#判断 if else
# if... elif....elif....elif...else
'''
xb = input("请输入性别：")
if xb == "男" :
    print("你的性别为男！！")
else:
    print("你的性别为女！！")
'''

cj = int(input("请输入成绩："))
if cj>=90 and cj<=100 :
    print("成绩优秀")
elif cj>=80 and cj<90 :
    print("成绩良好")
elif cj>=60 and cj<80 :
    print("成绩及格")
elif cj<60 :
    print("成绩不及格")
else:
    print("成绩输入有误！！")

