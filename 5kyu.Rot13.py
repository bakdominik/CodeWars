from CodeWarsTests import * 
import string

def rot13(message):
    letters = list(string.ascii_lowercase)
    new = ""
    for i in message:
        if i.lower() not in letters:
            new += i
        elif i == i.lower():
            new += letters[(letters.index(i.lower())+13)%26]
        else:
            new += letters[(letters.index(i.lower())+13)%26].upper()
    print(new)
    return new




test = Test()
test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")