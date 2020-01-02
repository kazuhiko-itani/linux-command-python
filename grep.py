import sys
import re

def main():
  args = sys.argv
  if len(args) == 2:
    sys.stderr.write(f'{__file__} need 3 arguments')
    return

  pattern = args[1]
  filename = args[2]

  do_grep(pattern, filename)

def do_grep(pattern, filename):
  dataList = []
  matchPattern = f'.*{pattern}.*'

  try:
    data = open(filename, "r")

    for line in data:
      result = re.match(matchPattern, line)

      if result: 
        dataList.append(line)

    for line in dataList:
      print(line)

  except:
    sys.stderr.write(f'{filename} is not file')
  else:
    data.close()

if __name__ == "__main__":
  main()
