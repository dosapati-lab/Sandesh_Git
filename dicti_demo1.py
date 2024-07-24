emp={
    "eid":"101",
    "ename":"kamal",
    "esal":19000,
    "age":35
}
dept={
    "did":"101",
    "dname":"csc",
    "dlocation":"hyd"
    }
print(emp["ename"],"::",dept["dname"])

for i in emp.keys(): # this function for grtting the keys
    print(i)

for j in emp.values(): # this function to get valus
    print("values :",j)

for k,y in emp.items():
    print(k,":",y) 