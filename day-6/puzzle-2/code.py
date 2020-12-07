import sys
import re

def main():

  # Read file
  file_name = sys.argv[1]
  input = []
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
      input.append(string)
  input[len(input)-1] += '\n'
  
  # Count number questions answered 'yes' within each group
  sum = 0
  for line in input:
    counter = 1
    member_count = 0
    sorted_string = sorted(line)
    prev = ''
    for char in sorted_string:
      if char == '\n':
        member_count += 1
      elif char == prev:
        counter += 1
      else:
        if counter == member_count:
          sum += 1
        counter = 1
      prev = char
    # Account for the very last question of each group
    # .. and the one member check is for single rows 
    # for which the last question is counted twice otherwise
    if counter == member_count and member_count > 1: 
      sum += 1

  print("%d all-yes-answered questions in total" % sum) 

# Input error handling
if (len(sys.argv) > 2) or (len(sys.argv) < 2):
  sys.stderr.write("Usage: python <code file> <input file>\n")
  sys.exit(1)

main()