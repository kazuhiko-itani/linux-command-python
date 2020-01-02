import sys

LINES = 10

def main():
  args = sys.argv

  if len(args) != 2:
    sys.stderr.write(f'{args[0]}: file name not given') 
    return

  tail(args[1])

def tail(filename):
  dataList = []
  count = 0
  readLines = 0

  try:
    data = open(filename, "r")

    for line in data:
      if readLines > LINES and count > LINES:
        count = 0
        dataList[count] = line

      elif readLines > LINES and count <= LINES:
        dataList[count] = line

      else:
        dataList.append(line)

      count += 1
      readLines += 1

    if readLines > LINES:
      for i in range(LINES):
        if count >= LINES:
          count = 0
        print(dataList[count], end="")
        count += 1

    else:
      for i in range(len(dataList)):
        print(dataList[i], end="")

  except Exception as e:
    print(e)
    sys.stderr.write(f'{filename} is not file')
  else:
    data.close()
    return dataList

if __name__ == "__main__":
  main()
