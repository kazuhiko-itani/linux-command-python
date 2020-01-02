"""Diplay the beginning of lines

usage: head.py [-h] [-n <N> | --lines <N>] [<file>...]

options:
    -h           show this help message and exit
    -n, --lines  number of rows to display
"""

import sys
from docopt import docopt

def main():
  args = docopt(__doc__)
  lines = int(args['<N>']) if args['<N>'] != None else 10

  if len(args['<file>']) == 0:
    for i in range(lines):
      print(input())

  else:
    for i in range(len(args['<file>'])):
      try:
        data = open(args['<file>'][i])

        for j, line in enumerate(data):
          if j >= lines:
            break

          print(line, end="")

      except:
        sys.stderr.write(f'{args["<file>"][i]} is not file')

      else:
        data.close()

if __name__ == "__main__":
  main()
