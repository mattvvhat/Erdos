"""
x_x
"""

def sum_digits(n):
  s = 0
  while n:
    n, remainder = divmod(n, 10)
    s += remainder
  return s


A = sum_digits(pow(3334, 3334))
B = sum_digits(A)
print 2013*sum_digits(B)
