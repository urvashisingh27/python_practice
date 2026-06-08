p1 = "make a lot of money"
p2 = "buy now"
p3 = "click this"

message = input ("enter your comment: ")

if (p1 in message or p2 in message or p3 in message):
    print("spam message")

else:
    print("clean message")

