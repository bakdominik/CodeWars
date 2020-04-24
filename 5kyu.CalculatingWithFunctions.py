from CodeWarsTests import *

def zero(x=""): return eval("0"+x)
def one(x=""): return eval("1"+x)
def two(x=""):return eval("2"+x)
def three(x=""): return eval("3"+x)
def four(x=""): return eval("4"+x)
def five(x=""): return eval("5"+x)
def six(x=""): return eval("6"+x)
def seven(x=""): return eval("7"+x)
def eight(x=""): return eval("8"+x)
def nine(x=""): return eval("9"+x)

def plus(x): return f"+{x}"
def minus(x): return f"-{x}"
def times(x): return f"*{x}"
def divided_by(x): return f"//{x}"



Test.describe('Basic Tests')
Test.assert_equals(seven(times(five())), 35)
Test.assert_equals(four(plus(nine())), 13)
Test.assert_equals(eight(minus(three())), 5)
Test.assert_equals(six(divided_by(two())), 3)