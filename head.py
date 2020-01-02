import sys

def main():
  args = sys.argv

  if len(args) < 2:
    sys.stderr.write(f'Usage: {args[0]} n [file file...]\n')
    return

  if len(args) == 2:
    for i in range(int(args[1])):
      print(input())

  else:
    for i in range(len(args) - 2):
      try:
        data = open(args[i + 2])

        for j, line in enumerate(data):
          if j >= int(args[1]):
            break

          print(line, end="")

      except:
        sys.stderr.write(f'{args[i + 2]} is not file')

      else:
        data.close()

if __name__ == "__main__":
  main()
