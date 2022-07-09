# Initialisation and declaration of user input to books
books = int(input('Enter Number of books purchased? '))
if books == 0:
    # declaration of variable n to represent points
    n = 0
    print("Points garnered are : " + str(n))
elif books == 1:
    n = 6
    print("Points garnered are : " + str(n))
elif books == 2:
    n = 16
    print("Points garnered are : " + str(n))
elif books == 3:
    n = 32
    print("Points garnered are : " + str(n))
elif books >= 4:
    n = 60
    print("Points garnered are : " + str(n))



