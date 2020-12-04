import sys
import re

def main():

  # Expected fields
  Fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

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
  
  # Parse input lines and check if they satisfy the requirements
  counter = 0
  print(len(List))
  for line in List:
    Found = [False] * len(Fields)
    Found[7] = True
    Res = re.split(":[a-zA-Z0-9#]+[ |\n]*", line)
    if len(Res) >= len(Fields) - 1:
      for i in range(len(Fields)):
        for res in Res:
          if res == Fields[i]:
            Found[i] = True
      valid = True
      for found in Found:
        valid = valid and found
      if valid:
        counter += 1
  
  print("%d valid passports" % counter) 

# Input error handling
if (len(sys.argv) > 2) or (len(sys.argv) < 2):
  sys.stderr.write("Usage: python <code file> <input file>\n")
  sys.exit(1)

main()