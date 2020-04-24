from CodeWarsTests import *


def solution(number):

    return sum(x for x in range(number) if x%3==0 or x % 5 == 0)


Test.describe("Multiples of 3 and 5")

Test.it("should handle basic cases")
Test.assert_equals(solution(10), 23)