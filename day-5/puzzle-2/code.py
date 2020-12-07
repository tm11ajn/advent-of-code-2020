import sys
import re

# Plane seat data
row_low = 0
row_high = 127
col_low = 0
col_high = 7


def main():

  # Read file
  file_name = sys.argv[1]
  file = open(file_name, 'r')
  List = file.readlines()
  file.close()
  
  # Compute all seat IDs
  Seatids = []
  for line in List:
    Seatids.append(find_seat_ID(line))
    
  # Sort the IDs
  Seatids.sort()

  # Find your seat ID
  previd = -1
  for id in Seatids:
    if id - previd == 2:
      print("%d is your seat ID" % (id - 1)) 
      sys.exit(0)
    previd = id


def find_seat_ID(line):
  indices = [[row_low, row_high], [col_low, col_high]]
  for char in line:
    if char == 'F':
      indices[0][1] -= (indices[0][1] - indices[0][0] + 1)/2
    elif char == 'B':
      indices[0][0] += (indices[0][1] - indices[0][0] + 1)/2
    elif char == 'L':
      indices[1][1] -= (indices[1][1] - indices[1][0] + 1)/2
    elif char == 'R':
      indices[1][0] += (indices[1][1] - indices[1][0] + 1)/2      
  seatid = indices[0][1] * 8 + indices[1][1]
  return seatid
    

# Input error handling
if (len(sys.argv) > 2) or (len(sys.argv) < 2):
  sys.stderr.write("Usage: python <code file> <input file>\n")
  sys.exit(1)

main()