a = int (input("enter your age: "))

#if statement independent of if2
if(a%2 == 0):
    print("a is even number")

#if statement independent of if1
if (a>18):
    print("you are above age")

elif (a<0): #there can be multiple elif statements in 1 if statement
    print("invalid age")

else:
    print("you are below age")

print("bye bye")