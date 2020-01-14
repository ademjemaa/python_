import sys

argv = sys.argv[1::]
argv = argv[::-1]
for ag in range(len(argv)):
    final = argv[ag][::-1]
    chars = list(final)
    for i in range(0, len(chars)):
        if ord(chars[i]) >= 97 and ord(chars[i]) <= 122:
            chars[i] = chr(ord(chars[i]) - 32)
        elif ord(chars[i]) >= 65 and ord(chars[i]) <= 90:
            chars[i] = chr(ord(chars[i]) + 32)
    print("".join(chars), end='')
    if ag != len(argv) - 1:
        print(" ", end='')
print("")
