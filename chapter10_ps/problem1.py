#func to find greatest number
def greatest_num(n1, n2, n3):
    if(n1>n2 and n2>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else:
        return n3
    
m1 = int (input("enter the number: "))
m2 = int (input("enter the number: "))
m3 = int (input("enter the number: "))

print(f"greatest number is: {greatest_num(m1,m2,m3)}")