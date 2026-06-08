a = int(input("enter 1st num= "))
b = int(input("enter 1st num= "))
c = int(input("enter 1st num= "))
d = int(input("enter 1st num= "))

if (a>b and a>c and a>d):
    print("greatest num is a: ", a)

elif (b>a and b>c and b>d):
    print("greatest num is b: ", b)

elif (c>b and c>a and a>d):
    print("greatest num is c: ", c)

else:
    print ("greatest num is D: ", d)  
