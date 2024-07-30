'''
recursion : it has to calling it self is called recursion
filter() -> it has to check thr conditions

map() -> it has to adding the additional output

lamda with if and else

l.sort() or sorted() -> by default ascending order(small to big)

reverse=True
example  : sorted(reverse=True) --> it ha to diplay the desceing order(big yo small)

reduse --> funtools
def add(x,y):
    return x+y
number_=[1,2,3,4,5]
x2=reduce(add,number)

x2=reduse(lamda x,y:x+y,number_)

lamda with for loop

NumPy  -> it's working for array's concept
how to install numpy pipe  --> install pip numpy
how to impot it --> import numpy
how to create object/refernce variable  ---> import numpy as np

How to create  zero matrix
Syntax: x1=np.array(30)  // zero matrix

'''''

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
x1=int(input("enter number:"))
print("factorial  number:",fact(x1))


# recursive string

def f1(s):
    if  len(s)==0:
        return s
    else:
        return s[-1] + f1(s[:-1])
s1=input("enter a string :: ")
s2=input("enter a string :: ")
s3=input("enter a string :: ")
s4=s1 + s2 +s3
print("reverse :: \n",f1(s4))

#fibonaci series in recursive

def f2(n):
    if n<1:
        return 1
    else:
        return f2(n-1) + f2(n-2)
n2=int(input("Enter a number ::"))
print("Fibonaci::\n",f2(n2))


# lamda anonums functions
x1=lambda x:x+10
print(x1(20))
#arthametic
a1=lambda x,y:x+y
b1=lambda x,y:x-y
c1=lambda x,y:x*y
d1=lambda x,y:x/y
print("add of \n",a1(10,20))
print("sub of \n",b1(10,20))
print("mul of \n",c1(10,20))
print("div of \n",d1(10,20))


# Filter Function

numbers_=[1,2,3,4,5]
even_list=list(filter(lambda num:num%2==0,numbers_))
odd_list=list(filter(lambda num:num%2!=0,numbers_))
print("Even list \n",even_list)
print("odd list \n",odd_list)

d1=[34,34,34]
stu_status=list(filter(lambda s:s<35, d1))
if stu_status==True:
    stu_status="pass"
    
else:
    stu_status="Fail"
print(stu_status)