from CodeWarsTests import * 


def max_sequence(seq):
    total_max = 0
    for left in range(len(seq)):
        current_sum = 0
        right = left
        while right < len(seq):
            current_sum += seq[right]
            total_max = max(current_sum,total_max)
            right += 1
    return total_max
        





test = Test()
test.describe("Tests")
test.it('should work on an empty array')   
test.assert_equals(max_sequence([]), 0)
test.it('should work on the example')
test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)