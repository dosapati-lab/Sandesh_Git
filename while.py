'''
control statement
#while
#hands on:
#write pyton program to check the given number  is amstrong or not using while
#input :153
#it's armstrong

#input :154
#it's not armstrong

#2) write python program to disply given number multifunction table 

#input:5
#5*1=1
#5*2=10)"""

# for  -->
# continu : if the condition  is false it has to continue the rest of the code

# break --->

# it has to just break the compailer then it has to get out 

# function :

# it has to create block of code 

# def f1:
     #our code

# there are diff funtions
# 1) no return type and no parameters
#  syntax ->   def  add():
# 2) with parameters and no return type.
# syntax -> def  emp(eid,ename,esal):

# 3)  with return type and no parameters 

# Syntax -> def status():
#                return true,
# 4) function with both with paramerts and returntype.
# Syntax -> def show(sid,sname,scourse):
#                return sid "::",sname "::"", scourse "::"
# / -> it will allows only arguments
# 5) def f2(x,/):
#         f2(10)   valid
#          f2(x=10)   invalid
#   def f3(ch1,ch2,ch3):
#        print(f1(ch1="app1",ch2="app2",ch3="app3"))

#  How to send mutilple arguments?
# syntax -> def  f3(*k):
#                f3("hello")
 #                f3("hello","bye")
#               f3("hello",,"bye,"bye")
#  How to pass key and value both here
# first "*" reprasent key
# second "*" reprasent Value
# def f4(**k):
#      print(k[lname])
#      f4(lname="san",fname="g",add="hyd")

'''
# type1 function

def f1():
    l=[]
    for i in range(10):
        if i==5:
            continue
        l.append(i)
    print(l)
        
def f2():
    l=[]
    for i in range(10):
        if i==5:
            break
        l.append(i)
    print(l)

# type 2 funcrtion

def emp(eid,ename,esal):
    l=[]
    l.append(eid)
    l.append(ename)
    l.append(esal)
    for x in l:
        print(x)
id=int(input("Enter id :"))
name=input("Enter Name :")
sal=int(input("Enter Sal :"))
emp(id,name,sal)

# type 3 return type no parameters

