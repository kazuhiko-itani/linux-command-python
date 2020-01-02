"""create directory

usage: mkdir.py [-h] [-p] <path>

options:
    -h           show this help message and exit
    -p           create directory recursive
"""

import sys
import os
from docopt import docopt

def main():
  args = docopt(__doc__)
  recursiveFlag = args['-p']

  mkdir(args['<path>'], recursiveFlag)


def mkdir(path, recursiveFlag):
  try:
    os.mkdir(path)
  except FileNotFoundError as e:
    if recursiveFlag:
      parentPath = path.split("/")
      parentPath.pop()
      parentPath = "/".join(parentPath)
      mkdir(parentPath, recursiveFlag)
      os.mkdir(path)
    else:
      sys.stderr.write(f'No such file or directory: {path}')

if __name__ == "__main__":
  main()
