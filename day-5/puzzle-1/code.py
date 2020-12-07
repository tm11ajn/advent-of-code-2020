import sys
import re

def main():

  # Plane seat data
  row_low = 0
  row_high = 127
  col_low = 0
  col_high = 7

  # Read file
  file_name = sys.argv[1]
  file = open(file_name, 'r')
  List = file.readlines()
  file.close()
  
  # Parse input lines and check if they satisfy the requirements
  max = 0
  for line in List:
    indices = [[row_low, row_high], [col_low, col_high]]
    for char in line:
      if char == 'F':
        indices[0][1] -= (indices[0][1] - indices[0][0])/2
      elif char == 'B':
        indices[0][0] += (indices[0][1] - indices[0][0])/2
      elif char == 'L':
        indices[1][1] -= (indices[1][1] - indices[1][0])/2
      elif char == 'R':
        indices[1][0] += (indices[1][1] - indices[1][0])/2      
    seatid = indices[0][1] * 8 + indices[1][1]
    if seatid > max:
      max = seatid
  
  print("%d is the max seat ID" % max) 

# Input error handling
if (len(sys.argv) > 2) or (len(sys.argv) < 2):
  sys.stderr.write("Usage: python <code file> <input file>\n")
  sys.exit(1)

main()