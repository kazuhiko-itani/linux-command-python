"""Display filename in target directory
  
usage: ls.py [-h] [-t] <dir>

options:
    -h  show this help message and exit
    -t  show files recursion
"""

import sys
import glob
from docopt import docopt

def main():
  args = docopt(__doc__)
  if args['<dir>'] == None:
    sys.stderr.write("dirname is not given")

  traverseFlag = args['-t']
  do_ls(args['<dir>'], traverseFlag)

def do_ls(path, traverseFlag):
  files = glob.glob(f'{path}/*')
  for file in files:
    try:
      print(file)
      open(file)
    except:
      if traverseFlag:
        do_ls(file, traverseFlag)
      else:
        continue

if __name__ == "__main__":
  main()
