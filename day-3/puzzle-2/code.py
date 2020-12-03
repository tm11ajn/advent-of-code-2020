import sys
import re

def main():

  # Constants for slope
  Right = [1, 3, 5, 7, 1]
  Down = [1, 1, 1, 1, 2]

  # Read file
  file_name = sys.argv[1]
  List = []
  with open(file_name, 'r') as file:
    while True:
      line = file.readline()
      if not line:
        break
      List.append(line)
  
  # Find map-specific parameters
  height = len(List)
  width = len(List[0]) - 1

  # For the various slopes ...
  total = 1
  for i in range(len(Right)):
    right = Right[i]
    down = Down[i]

    # ... count trees
    counter = 0
    x = 0
    y = 0
    while y < height:
      if ((List[y])[x] == '#'):
        counter = counter + 1
      x = (x + right) % width
      y = y + down

    total = total * counter
  
  print("%d" % total) 

# Input error handling
if (len(sys.argv) > 2) or (len(sys.argv) < 2):
  sys.stderr.write("Usage: python <code file> <input file>\n")
  sys.exit(1)

main()