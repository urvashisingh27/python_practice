def celsiusToFah(degree):
    fahrenheit = degree*(9/5)+32
    return fahrenheit

degree = int(input("enter the celsius: "))
print(celsiusToFah(degree))