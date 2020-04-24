from CodeWarsTests import *


''''Move the first letter of each word to the end of it, then add "ay" to the 
end of the word. Leave punctuation marks untouched.'''

def pig_it(text):
    words = text.split()
    result = ""
    marks = [".","?","!"]
    for i in range(len(words)):
        if words[i] not in marks:
            words[i] = words[i][1:] + words[i][0] + "ay"

    return " ".join(words)        


Test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
Test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')