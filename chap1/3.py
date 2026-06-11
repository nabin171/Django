#write a python program to print the contents of a directory using the os modules .

import os

directory_path="/1.py"


content=os.listdir(directory_path)

for item in content:
    print(item)