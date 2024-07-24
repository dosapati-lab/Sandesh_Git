t1=(10,20,30,True,"hello",10.5,10,10)
t2=21,22,34
t3=()
t4=(31,)
t5=t1 + t2 + t3 + t4
print("after adding 4 obj :",t5)
print("0th index value :",t5[0])
print(" -1 index value : ",t5[-1])
print("slice operator : ",t5[1:5]) # 5th index not included
print("slice :",t5[1:]) # it will disply from 1th index to  upto last
print("slice : ",t5[:3]) # it will disply upto 2nd index

for x in t5:
    print(x)

l1=list(t5) # this function help to convert tuple function to list
l1[0]=45
print("after updating oth index element :", l1)
l1.pop()
print("remove the lat element:",l1) # it will remove the last element


