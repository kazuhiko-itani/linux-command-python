import sys

def main():
  args = sys.argv

  if len(args) < 2:
    print(f'{args[0]}: file name not given')
    return

  for i in range(len(args)):
    if i == 0:
      continue

    do_cat(args[i])

def do_cat(filename):
  try:
    data = open(filename, "r")

    for line in data:
      print(line, end="")
  except:
    print(f'{filename} is not file');
  else:
    data.close()

if __name__ == "__main__":
  main()
  
