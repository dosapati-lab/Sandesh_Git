def f3():
     return "welcome"

def f5():
     return "hello"
    

def f4():
    s=f3() + f5()
    #b1=bytearray(s)
    for x in s:
        print(ord(x),"::",x)

f4()