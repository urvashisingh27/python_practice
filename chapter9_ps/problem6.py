i = 1
n = int(input("enter number: "))

for i in range(1, n):
#while(i<n):
    n *= i
    #i += 1
else:
    print("factorial is: ", n)