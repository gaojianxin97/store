# 衣服
mc1 = "羽绒服"
mc2 = "牛仔裤"
mc3 = "风衣"
mc4 = "皮草"
mc5 = "T恤"
mc6 = "衬衫"
jg1 = 253.6
jg2 = 86.3
jg3 = 96.3
jg4 = 135.9
jg5 = 65.8
jg6 = 49.3
kc1 = 500
kc2 = 600
kc3 = 335
kc4 = 855
kc5 = 632
kc6 = 562
xl1 = 10 + 69 + 140 + 10 + 10
xl2 = 60 + 72 + 35 + 90 + 60 + 60 + 140
xl3 = 43 + 25 + 43 + 60 + 43 + 78
xl4 = 63 + 24 + 63 + 57
xl5 = 63 + 45 + 129 + 63 + 58 + 48 + 63
xl6 = 120
print(
    "羽绒服的销售额占比：",
    round((jg1 * xl1)/(jg1*xl1+jg2*xl2+jg3*xl3+jg4*xl4+jg5*xl5+jg6*xl6) * 100,2),"%",
    "\t\t" "销售占比：",
    round((xl1/(xl1+xl2+xl3+xl4+xl5+xl6)) * 100,2),"%",
)
print(
    "牛仔库的销售额占比：",
    round((jg2 * xl2)/(jg1*xl1+jg2*xl2+jg3*xl3+jg4*xl4+jg5*xl5+jg6*xl6) * 100,2),"%",
    "\t\t" "销售占比：",
    round((xl2/(xl1+xl2+xl3+xl4+xl5+xl6)) * 100,2),"%",
)
print(
    "风衣的销售额占比：",
    round((jg3 * xl3)/(jg1*xl1+jg2*xl2+jg3*xl3+jg4*xl4+jg5*xl5+jg6*xl6) * 100,2),"%",
    "\t\t\t" "销售占比：",
    round((xl3/(xl1+xl2+xl3+xl4+xl5+xl6)) * 100,2),"%",
)
print(
    "皮草的销售额占比：",
    round((jg4 * xl4)/(jg1*xl1+jg2*xl2+jg3*xl3+jg4*xl4+jg5*xl5+jg6*xl6) * 100,2),"%",
    "\t\t\t" "销售占比：",
    round((xl4/(xl1+xl2+xl3+xl4+xl5+xl6)) * 100,2),"%",
)
print(
    "T恤的销售额占比：",
    round((jg5 * xl5)/(jg1*xl1+jg2*xl2+jg3*xl3+jg4*xl4+jg5*xl5+jg6*xl6) * 100,2),"%",
    "\t\t\t" "销售占比：",
    round((xl5/(xl1+xl2+xl3+xl4+xl5+xl6)) * 100,2),"%",
)
print(
    "衬衫的销售额占比：",
    round((jg6 * xl6)/(jg1*xl1+jg2*xl2+jg3*xl3+jg4*xl4+jg5*xl5+jg6*xl6) * 100,2),"%",
    "\t\t\t" "销售占比：",
    round((xl6/(xl1+xl2+xl3+xl4+xl5+xl6)) * 100,2),"%",
)