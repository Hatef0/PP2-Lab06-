## Python Directories and Files.

## 1)List only directories, files and all in a path.

import os

path = "."
print("Directories:", [d for d in os.listdir(path) if os.path.isdir(d)])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(f)])
print("All:", os.listdir(path))


## 2)Check access to a specified path.

import os

path = input("Enter path: ")
print("Exists:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))


## 3)Test if path exists, get filename and directory.

import os

path = input("Enter path: ")
if os.path.exists(path):
    print("Filename:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("Path does not exist")


## 4)Count number of lines in a text file.

file = input("Enter filename: ")
with open(file, 'r') as f:
    print("Number of lines:", sum(1 for line in f))


## 5)Write a list to a file.

data = ["Apple", "Banana", "Cherry"]
with open("fruits.txt", "w") as f:
    for item in data:
        f.write(item + "\n")


## 6)Generate 26 text files A.txt to Z.txt .

import string

for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").close()


## 7)Copy contents of one file to another.

src = input("Enter source filename: ")
dst = input("Enter destination filename: ")

with open(src, 'r') as f1, open(dst, 'w') as f2:
    f2.write(f1.read())


## 8)Delete file by specified path (check access first).

import os

path = input("Enter file path: ")
if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted successfully")
    else:
        print("No permission to delete this file")
else:
    print("File does not exist")

    
