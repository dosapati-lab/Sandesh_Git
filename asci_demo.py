"""
x1=" hello ".strip()
x2=" welcome ".strip()
x3=" hyd ".strip()
x4=x1 + x2 + x3
print("after adding 3 obj : ",x4)
for i in x4:
    print(i,"asci codes : ",ord(i))

    """

x1=" hello.sandy.ramu. ".strip()
x2=" welcome.ramu.obj. ".strip()
x3=" hyd.city.bye. ".strip()
x4=x1 + x2 + x3
print("after adding 3 obj : ",x4)
for i in x4.split("."):
    print(i)