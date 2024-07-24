#x1=[1,"app",0.5,True,"bye"]
#print("list :",type(x2))
x2=[1,"app",1,"app",0.5,0.5,True,False,True]
#print(x1)
print(x2)
for i in x2:
    print(i)
s=int(input("start range"))
n=int(input("ends range"))
for k in range(s,n):
    x2.append(k)
print("after adding dynaminc elements",x2)
