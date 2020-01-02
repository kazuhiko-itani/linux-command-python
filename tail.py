"""Diplay the end of lines
  
usage: tail.py [-h] [-n <N> | --lines <N>] <file>

options:
    -h           show this help message and exit
    -n, --lines  number of rows to display
"""

import sys
from docopt import docopt

DEFAULT_LINES = 10

def main():
  args = docopt(__doc__)
  lines = int(args['<N>']) if args['<N>'] != None else DEFAULT_LINES

  if args['<file>'] == None:
    sys.stderr.write(f'{__file__}: file name not given') 
    return

  tail(args['<file>'], lines)

def tail(filename, lines):
  dataList = []
  count = 0
  readLines = 0

  try:
    data = open(filename, "r")

    # store data
    for line in data:
      if readLines > lines:
        dataList[count] = line
      else:
        dataList.append(line)

      count += 1
      readLines += 1

      if count > lines:
        count = 0

    # display data
    if readLines > lines:
      for i in range(lines):
        if count >= lines:
          count = 0
        print(dataList[count], end="")
        count += 1

    else:
      for i in range(len(dataList)):
        print(dataList[i], end="")

  except:
    sys.stderr.write(f'{filename} is not file')
  else:
    data.close()

if __name__ == "__main__":
  main()
