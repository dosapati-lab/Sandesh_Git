x1=[1,"app1","app2","bye",2,"bye2"]
x2=[10,20,30]
x1.extend(x2)
print(" after Adding : ",x1)
x1.pop()
print(" after calling pop : ",x1)
x1.remove("bye")
print("after calling remove : ",x1)
x2.sort()
print("after calling sort assending order :",x2)
x2.sort(reverse=True)
print("after calling sort desending order :",x2)
x1.insert(2,"100")
print("after calling insert : ",x1)
x1.clear()
print("adter calling clear :",x1)
