import string

t = (19, 42, 21)
print("The " + str(len(t)) + " numbers are: ", end='')
for i in range(len(t)):
    print(t[i], end='')
    if i != len(t) - 1:
        print(", ", end='')
print()
