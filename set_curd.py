s1={"apple"}
c=0
for x in range(5):
    print("1. adding elemet  ")
    print("2. Deleting given elemet  ")
    print("3. Displaying elemet  ")
    print("4. update given elemet  ")
    print("5. Exit the Menu  ")
    print("6. search the given element  ")
    n1=input("Enter your choice :: ")
    match n1:
        case "1":
            ele=input("Enter Ele :: ")
            s1.add(ele)
        case "2":
            ele2=input("Enter Ele for delete :: ")
            s1.remove(ele2)
        case "3":
            for i in s1:
                print(i)
        case "4":
            l1=list(s1)
            n1=int(input("Enetr a index for updating ele :: "))
            up=input("Enter a update Ele :: ")
            l1[n1]=up
            s1=set(l1)
        case "5":
            exit(0)
        case  "6":
            s4 =input("Enter Searching Element :")
            for x1 in s1:
                if x1==s4:
                    c=c+1
                else:
                    c=0
            if c==1:
                print("the element is found")
            else:
                print("the Element is not Found")