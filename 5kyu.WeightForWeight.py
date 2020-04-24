from CodeWarsTests import * 



def order_weight(strng):
    # your code
    bar = sorted(strng.split(' '))
    baz = sorted(bar, key=lambda n: sum([int(item) for item in n]))
    return " ".join(baz)

            
Test.it("Basic tests")
Test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
Test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
