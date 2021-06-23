def main(*args, **kwargs):
  for arg in args:
    print(arg)

  for name, arg in kwargs.items():
    print(f'{name} = {arg}')

if __name__ == '__main__':
  main(1, 2, 3, a="hello", b="world!")
