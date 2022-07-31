def fizzbuzz(n: int, a: str = "Fizz", b: str = "Buzz", c: str = "Baxx"):
  print(*
    [((a * (i % 3 == 0)) + (b * (i % 5 == 0)) + (c * (i % 7 == 0))) or i for i in range(1, n + 1)],
    sep="\n"
  )

if __name__ == '__main__':
  fizzbuzz(20)
