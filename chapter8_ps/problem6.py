marks = int(input("enter the number: "))

if(marks <= 100 and marks >= 90):
    print("grade = A")

elif(marks < 90 and marks >= 80):
    print("grade = B")

elif(marks < 80 and marks >= 70):
    print("grade = C")

elif(marks < 70 and marks >= 60):
    print("grade = D")

elif(marks < 60 and marks >= 50):
    print("grade = E")

elif(marks < 50):
    print("grade = F")