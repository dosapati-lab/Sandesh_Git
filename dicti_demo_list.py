student={
       "name":"ravi",
       "phno":9492967715,
       "cources":["java","python","dotnet","php"]
}
print("name :",student["name"])
print("Phone No :",student["phno"])
print("Cources :",student["cources"])

print("after updating :")
student["name"] = "pavan"
student["phno"] = "123456777"
student["cources"] = "java"

print("name :",student["name"])
print("Phone No :",student["phno"])
print("Cources :",student["cources"])

d1={
    "sid":101,
    "sname":"sname",
    "sid":102,
    "scource":"sanme",
}
print(d1)
print(d1.get("scource"))
print(d1.pop())
print(d1.clear())