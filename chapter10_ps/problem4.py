#recursion usage

def sum(num):
    if(num == 1):
        return 1
    return sum(num-1)+num



num = int(input("enter number: "))
print(sum(num))