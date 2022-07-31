BLOCKS = [
 ('BO'),
 ('XK'),
 ('DQ'),
 ('CP'),
 ('NA'),
 ('GT'),
 ('RE'),
 ('TG'),
 ('QD'),
 ('FS'),
 ('JW'),
 ('HU'),
 ('VI'),
 ('AN'),
 ('OB'),
 ('ER'),
 ('FS'),
 ('LY'),
 ('PC'),
 ('ZM'),
]

def main(words):
  for word in words:
    print(f'{word} -> {make(word)}')

def make(word, blocks = BLOCKS):
  if not word:
    return []

  first, rest = word[0], word[1:]

  for i in range(len(blocks)):
    if first in blocks[i] and (res := make(rest, blocks[0:i] + blocks[i+1:])) != None:
      return [blocks[i]] + res

if __name__ == '__main__':
  main(["A", "BARK", "BOOK", "TREAT", "COMMON", "SQUAD", "CONFUSE"])
