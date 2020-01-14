import string
import sys


def calcul(one, two):
    print("Sum:\t\t" + str(int(one) + int(two)))
    print("Difference:\t" + str(int(one) - int(two)))
    print("Product:\t" + str(int(one) * int(two)))
    if int(two) != 0:
        print("Quotient:\t" + str(int(one) / int(two)))
    else:
        print("ERROR (div by zero)")
    if int(two) == 0:
        print("ERROR (modulo by zero)")
    else:
        print("Remainder:\t" + str(int(one) % int(two)))


argv = sys.argv[1::]
if len(argv) == 2 and argv[0].isnumeric() and argv[1].isnumeric():
    calcul(argv[0], argv[1])
else:
    print("InputError: only numbers\n\nUsage: python operations.py")
    print("Example:\n\tpython operations.py 10 3")
