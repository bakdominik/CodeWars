from CodeWarsTests import *

def valid_parentheses(string):
    opened = 0
    to_close = 0
    closed = 0
    for char in string:
        if char == "(":
            opened += 1
            to_close += 1
        if char == ")":
            if to_close:
                to_close -= 1
            else:
                return False
            closed +=1
    
    return opened == closed and to_close == 0






Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)