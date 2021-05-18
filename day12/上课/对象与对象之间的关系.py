'''
    用户：
        id,姓名，年龄，性别，体重
    地址：
        国家，省份，街道，门牌号
    关系：包含



'''
class  User:
    id = ""
    username = ""
    age = 0
    sex = ""
    weight = 0.0
    address = None  # 包含的是其他对象，就应该写None   ""

class Address:
    country = ""
    province = ""
    street = ""
    door = ""

add = Address()
add.country = "cn"
add.province = "anhui"
add.street = "幸福大道"
add.door = "s001"

u = User()
u.id = 1
u.username = "jason"
u.weight = 70.4
u.sex = "男"
u.age = 89
u.address = add


print(u.address.country)














