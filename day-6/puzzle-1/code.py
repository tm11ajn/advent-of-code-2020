import sys
import re

def main():

  # Read file
  file_name = sys.argv[1]
  List = []
  done = False
  with open(file_name, 'r') as file:
    while not done:
      string = ""
      while True:
        line = file.readline()
        if not line:
          done = True
          break
        if line == "\n":
          break
        string += line
      List.append(string)
  
  # Count number of yes'd questions within each group
  sum = 0
  for line in List:
    counter = 0
    Sorted = sorted(line)
    prev = ''
    for s in Sorted:
      if not s == prev and not s == '\n':
        counter += 1
      prev = s
    sum += counter

  print("%d yes-answered questions in total" % sum) 

# Input error handling
if (len(sys.argv) > 2) or (len(sys.argv) < 2):
  sys.stderr.write("Usage: python <code file> <input file>\n")
  sys.exit(1)

main()