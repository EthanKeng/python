#learning how to play with datetime module

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,"w") as f:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  rft = datetime.datetime.fromtimestamp(timestamp)
  result = str(rft)[:10]
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return result

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
