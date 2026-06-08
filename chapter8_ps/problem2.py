m1 = float(input("enter marks of 1st subj: "))
m2 = float(input("enter marks of 2nd subj: "))
m3 = float(input("enter marks of 3rd subj: "))

total_percentage = (m1 + m2 +m3)/3



if (m1>33 and m2>33 and m3 > 33 and total_percentage>40):
    print("student is passed")

else:
    print("student is failed")