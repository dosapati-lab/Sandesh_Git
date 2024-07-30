'''
how to use ifelse condition in lambda
'''
even_odd=(lambda x:"Even" if x%2==0 else "odd")

print(even_odd(10))

'''
How to use netsed if else conditions

'''

chk_age=(lambda age:"child"  if age<10 else("tenage" if age<25 else("youth" if age<45 else "senior")))

x1=int(input("enter age ::\n"))
print(chk_age(x1))


Grade=(lambda marks:"A"  if marks>75 else("B" if marks>60 else("C" if marks>35 else "Fail")))

x1=int(input("enter Marks ::\n"))
print("Grade ::", Grade(x1))

