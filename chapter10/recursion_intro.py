def fact(n):
    if(n == 1 or n == 0):
        return 1
    return n*fact(n-1)

m = int (input("enter the number: "))
print(f"factorial of number {m} is: {fact(m)}")