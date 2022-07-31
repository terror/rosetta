def main(a, b):
  return {k: v for k, v in zip(a, b)}

if __name__ == '__main__':
  print(main([1, 2, 3], [4, 5, 6]))
