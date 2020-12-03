import sys
import re

# Finds the three numbers of the input list that sum
# to 2020 and outputs their product.
def main():

  # Read file
  file_name = sys.argv[1]
  List = []
  with open(file_name, 'r') as file:
    while True:
      line = file.readline()
      if not line:
        break
      List.append(int(line))
  
  # Sort input
  List.sort(reverse=True)
  
  # Check possible combinations
  length = len(List)
  for item in List:
    i = length - 1
    j = length - 1
    while (i > -1) and (item * 3 > 2020) and (item + List[i] + List[j] < 2020):
      j = length - 1
      while (j > -1) and (item * List[i] * 2 < 2020) and (item + List[i] + List[j] < 2020):
        j = j - 1
      i = i - 1

    if i != j and (item + List[i] + List[j]) == 2020:
      print("%d %d %d" % (item, List[i], List[j]))
      print(item * List[i] * List[j])
      sys.exit(0)    

# Input error handling
if (len(sys.argv) > 2) or (len(sys.argv) < 2):
  sys.stderr.write("Usage: python <code file> <input file>\n")
  sys.exit(1)

main()