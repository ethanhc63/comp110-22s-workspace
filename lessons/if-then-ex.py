"""Practice with if-then-else statements."""

choice: int = int(input("Enter a number: "))

if choice >= 50:
    if choice > 75:
        print("C")
    else: 
        print("D")
else:
    if choice < 25:
        print("A")
    else: 
        print("B")
