import string


def text_analyzer(text=''):
    while text == '':
        text = input("What is the text to analyse?\n")
    punct = 0
    upper = 0
    lower = 0
    space = 0
    for i in text:
        if i in string.punctuation:
            punct = punct + 1
        if i.isupper():
            upper = upper + 1
        if i.islower():
            lower = lower + 1
        if i == ' ':
            space = space + 1
    print("The text contains " + str(len(text)) + " characters:")
    print("- " + str(upper) + " upper letters")
    print("- " + str(lower) + " lower letters")
    print("- " + str(punct) + " punctuation marks")
    print("- " + str(space) + " spaces")
