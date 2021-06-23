import random

INFO = """How to play:
  - Receive four random numbers
  - Attempt to derive a mathematical expression with those numbers that results
    to 24
  - Try again

 :: 24 ::
"""

def check(expr, nums):
  for num in nums:
    if str(num) not in expr:
      return (True, f'{num} must be in the expression.')

  for num in [*range(1, 9)]:
    if str(num) in expr and num not in nums:
      return (True, f'{num} cannot be in the expression.')

  return (False, expr)

def main():
  print(INFO)
  while True:
    print(*(nums := [random.randint(0, 9) for _ in range(4)]))

    err, data = check(input('Expression: '), nums)
    if err:
      print(data, "\n")
      continue

    if (res := eval(data)) == 24:
      print('Win!')
      break

    print(f'Value: {res}, Off by: {abs(res - 24)}. Try again!\n')

if __name__ == '__main__':
  main()
