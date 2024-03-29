"""
Problem 6 - Sum square difference

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2.... 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 .. +10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is .
3025 - 385 = 2640

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""

#%%
def diff_sqrSum_sumSqr(n):
    sumSqr = sum([x ** 2 for x in range(1, n + 1)])
    sqrSum = sum(range(1, n + 1)) ** 2
    diff = sqrSum - sumSqr
    return diff


n = 100
diff_sqrSum_sumSqr(n)