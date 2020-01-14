import sys
import string
argv = sys.argv[1::]
if len(argv) == 2 and argv[1].isnumeric() and not argv[0].isnumeric():
    for i in string.punctuation:
        argv[0] = argv[0].translate(str.maketrans(i, ' '))
    res = argv[0].split()
    t = []
    for i in res:
        if len(i) > int(argv[1]):
            t.append(i)
    print(t)
else:
    print("ERROR")
