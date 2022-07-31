def unique(n) -> bool:
  return len(set(str(n))) == len(str(n))

def div(n) -> bool:
  digs = list(map(int, str(n)))
  print(digs)
  for dig in digs:
    if n & dig:
      return False
  return True

def main(start):
  while 1:
    if '0' in str(start):
      start += 1
      continue
    if unique(start) and div(start):
      return start
    start += 1

if __name__ == '__main__':
  print(main(0))
