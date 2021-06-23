import unittest

class TestGapful(unittest.TestCase):
  def setUp(self):
    self.data = {
      187:  True,
      190:  True,
      120:  True,
      478:  False,
      1:    True,
      777:  False,
      22:   True,
      4587: False
    }

  def runTest(self):
    for k, v in self.data.items():
      assert gapful(str(k)) == v

def gapful(n: str) -> bool:
  if len(n) <= 2:
    return True
  return int(n) % int(n[0] + n[-1]) == 0

def task(n, s):
  c = 0; ret = []
  while c < s:
    if gapful(str(n)):
      ret.append(n)
      c += 1
    n += 1
  return ret

def main():
  print(f'[Task #1]: {task(100, 30)}')
  print(f'[Task #2]: {task(1000000, 15)}')
  print(f'[Task #3]: {task(1000000000, 10)}')

if __name__ == '__main__':
  main()
