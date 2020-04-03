from CodeWarsTests import *
import numpy as np
import itertools


def enum(n):
    
       # base case of recursion: zero is the sum of the empty list
        if n == 0:
            yield []
            return

        # modify partitions of n-1 to form partitions of n
        for p in enum(n-1):
            yield [1] + p
            if p and (len(p) < 2 or p[1] > p[0]):
                yield [p[0] + 1] + p[1:]

def prod(n):
    prod = []
    for p in enum(n):
        prod.append(np.prod(p))
    
    return sorted(list(set(prod)))

def part(n):
    n = prod(n)
    return f"Range: {max(n)-min(n)} Average: {np.mean(n):.2f} Median: {np.median(n):.2f}"



Test.describe("Basic tests")
Test.it("Small numbers")

Test.assert_equals(part(1), "Range: 0 Average: 1.00 Median: 1.00")
Test.assert_equals(part(2), "Range: 1 Average: 1.50 Median: 1.50")
Test.assert_equals(part(3), "Range: 2 Average: 2.00 Median: 2.00")
Test.assert_equals(part(4), "Range: 3 Average: 2.50 Median: 2.50")
Test.assert_equals(part(5), "Range: 5 Average: 3.50 Median: 3.50")
