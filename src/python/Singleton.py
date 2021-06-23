class S:
  def __init__(self, d):
    self._d = d

  def __call__(self, d):
    raise TypeError('Call instance() instead!')

  def __instancecheck__(self, o):
    return instance(o, self._d)

  def instance(self, *args, **kwargs):
    if not hasattr(self, '_instance'):
      self._instance = self._d(*args, **kwargs)
    return self._instance

@S
class O:
  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return f'O: data={self.data}'

def main():
  f = O.instance(2)
  g = O.instance(1)

  print(f is g)

if __name__ == '__main__':
  main()
