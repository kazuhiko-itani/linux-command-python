import sys
import glob

def main():
  args = sys.argv

  files = glob.glob(f'{args[1]}/*')
  for file in files:
    print(file)

if __name__ == "__main__":
  main()
