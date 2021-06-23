def f(n):
  def g(i):
    nonlocal n
    n += i
    return n
  return g

def main():
  acc = f(1)
  acc(5)
  f(3)
  print(acc(2.3)) # 8.3

if __name__ == '__main__':
  main()
