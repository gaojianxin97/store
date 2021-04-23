List=[1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# list(set(List))  删除数组中相同的元素
List1=list(set(List))     # List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# len(List1)   List数组中元素的个数
a = len(List1)
b = 0
while b<a:
 # List.count(List1[b]): List=[1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]中出现[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]的次数
    print(List1[b],"出现",List.count(List1[b]),"次")
    b = b + 1