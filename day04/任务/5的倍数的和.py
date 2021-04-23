a = [1,5,21,30,15,9,30,24]
b = len(a)  # b=8
c = 0
d = 0
while c < b:
    if (a[c]) % 5 == 0 :
        d = d + a[c]
        c = c + 1
    elif (a[c]) % 5 != 0 :
        c = c + 1
print("5的倍数总和为：",d)