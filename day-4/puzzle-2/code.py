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
  print(len(List))
  
  # Parse input lines and check if they satisfy the requirements
  counter = 0
  for line in List:
    Found = [False] * len(Fields)
    Checked = [False] * len(Fields)
    Found[7] = Checked[7] = True
    Res = re.split(":|[ |\n]+", line)
    if len(Res) >= (len(Fields) - 1)*2:
      for i in range(int((len(Res)-1)/2)):
        for res in Res:
          if res == Fields[i]:
            Found[i] = True
            Checked[i] = check(Res[2*i], Res[2*i+1])
      valid = True
      for checked in Checked:
        valid = valid and checked
      if valid:
        counter += 1
  
  print("%d valid passports" % counter) 

def check(field, value):
  Eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  Fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

  if field == Fields[0]:
    matched = re.fullmatch("[0-9]{4}", value)
    if matched == None:
      return False
    val = int(value)
    return (val >= 1920 and val <= 2002)
 
  if field == Fields[1]:
    matched = re.fullmatch("[0-9]{4}", value)
    if matched == None:
      return False
    val = int(value)
    return (val >= 2010 and val <= 2020)
    
  if field == Fields[2]:
    matched = re.fullmatch("[0-9]{4}", value)
    if matched == None:
      return False
    val = int(value)
    return (val >= 2020 and val <= 2030)

  if field == Fields[3]:
    matched = re.fullmatch("[0-9]{2,3}(cm|in)", value)
    if matched == None:
      return False
    unit = re.search("(cm|in)", value)
    number = re.search("[0-9]{2,3}", value)
    val = int(number.group(0))
    if unit.group(0) == "cm":
      return (val >= 150 and val <= 193)
    return (val >= 59 and val <= 76)

  if field == Fields[4]:
    matched = re.fullmatch("#[0-9a-f]{6}", value)
    if matched == None:
      return False
    return True
    
  if field == Fields[5]:
    for eye in Eyes:
      if value == eye:
        return True
    return False          

  if field == Fields[6]:
    matched = re.fullmatch("[0-9]{9}", value)
    if matched == None:
      return False
    return True    

  if field == Fields[7]:
    return True

  return False

# Input error handling
if (len(sys.argv) > 2) or (len(sys.argv) < 2):
  sys.stderr.write("Usage: python <code file> <input file>\n")
  sys.exit(1)

main()