
"""
Fibonacci number generator
When given a position, the function returns the fibonacci at that position in the sequence.
The zeroth number in the fibonacci sequence is 0. The first number is 1
Negative numbers should return None
"""
def fibonacci(position):
  if position < 0:
    return None
  elif position == 0:
    return 0
  elif position == 1:
    return 1
  else:
    return fibonacci(position - 1) + fibonacci(position - 2)




