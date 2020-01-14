import sys

argv = sys.argv[1::]
if len(argv) > 1:
    print("ERROR")
elif argv[0].isnumeric():
    if int(argv[0]) == 0:
        print("I'm Zero.")
    elif int(argv[0]) % 2 == 0:
        print("I'm Even.")
    elif int(argv[0]) % 2 == 1:
        print("I'm Odd.")
else:
    print("Error")
