#exercise
#Create a new text file and draw a tree in it.
import os
import platform

if platform.system() == 'Windows':
    file_path = r'C:\Users\Mysha\Documents\some.txt'
else:
    file_path = 'some.txt'  # Linux / Codespace friendly

tree_string = (
    "   *   \n"
    "  ***  \n"
    " ***** \n"
    "*******\n"
    "  |||  \n"
)

with open(file_path, 'w') as tree_file:
    tree_file.write(tree_string)
