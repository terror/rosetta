def main(func):
  def wrap(*args, **kwargs):
    print('higher order!')
    return func(*args, **kwargs)
  return wrap

@main
def add(a, b):
  return a + b

if __name__ == '__main__':
  print(add(1, 2))
