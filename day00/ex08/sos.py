import sys
MORSE = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}
argv = sys.argv[1::]
var = ''
for ag in range(len(argv)):
    chars = list(argv[ag])
    code = ''
    for i in range(0, len(chars)):
        if chars[i].isalnum():
            if (ord(chars[i]) >= 97 and ord(chars[i]) <= 122):
                chars[i] = chr(ord(chars[i]) - 32)
            code = code + MORSE[chars[i]]
            code = code + ' '
        elif chars[i] == ' ':
            code = code + '/ '
        else:
            print("ERROR")
            quit()
    var = var + code + '/ '
var = var[:-3]
print(var)
