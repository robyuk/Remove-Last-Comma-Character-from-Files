#! /bin/env /usr/bin/python
#
# Remove the last character if it is a comma (,) from each file in a directory

from pathlib import Path

filesDir=Path('Files')
for filename in filesDir.iterdir():
  with open(filename, 'r') as file:
    content = file.read()
  
  if content[-1] == ',':
    with open(filename, 'w') as file:
      file.write(content[:-1])