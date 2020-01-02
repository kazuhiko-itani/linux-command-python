"""Search target character in file
  
usage: grep.py [-v] [-i] <pattern> <file>

options:
    -v  search not match line        
    -i  ignore case
"""

import sys
import re
from docopt import docopt

def main():
  args = docopt(__doc__)
  ignoreFlag = args['-i']
  inversionFlag = args['-v']

  if not args['<pattern>']:
    sys.stderr.write(f'{__file__} search charcter not given')
    return

  if not args['<file>']:
    sys.stderr.write(f'{__file__} file name not given')
    return

  do_grep(args['<pattern>'], args['<file>'], ignoreFlag, inversionFlag)

def do_grep(pattern, filename, ignoreFlag, inversionFlag):
  dataList = []
  matchPattern = f'.*{pattern}.*'

  try:
    data = open(filename, "r")

    for line in data:
      result = re.match(matchPattern, line)
      if ignoreFlag:
        result = re.match(matchPattern, line, re.IGNORECASE)

      if inversionFlag:
        if not result:
          dataList.append(line)
      else:
        if result: 
          dataList.append(line)

    for line in dataList:
      print(line, end="")

  except:
    sys.stderr.write(f'{filename} is not file')
  else:
    data.close()

if __name__ == "__main__":
  main()
