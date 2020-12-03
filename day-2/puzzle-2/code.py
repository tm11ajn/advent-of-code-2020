import sys
import re

def main():

  # Read file
  file_name = sys.argv[1]
  List = []
  with open(file_name, 'r') as file:
    while True:
      line = file.readline()
      if not line:
        break
      List.append(line)
  
  # Parse input lines and check if they satisfy the requirements
  counter = 0
  for line in List:
    res = re.split("[-|: | |\n]+", line)
    lower_bound = int(res[0])
    upper_bound = int(res[1])
    char = res[2]
    string = res[3]
#    print("%s %s %s %s" % (string[lower_bound-1], string[upper_bound-1], char, string))
    if (string[lower_bound - 1] == char) ^ (string[upper_bound - 1] == char):
      counter = counter + 1
  
  print("%d correct passwords" % counter) 

# Input error handling
if (len(sys.argv) > 2) or (len(sys.argv) < 2):
  sys.stderr.write("Usage: python <code file> <input file>\n")
  sys.exit(1)

main()