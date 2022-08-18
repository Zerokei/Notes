import os
import sys
import proc

# argv[1]: target dir

root = sys.argv[1]
dir_lists = os.walk(root)

# Iterate over all files
for dir, _, files in dir_lists:
    for f in files:
        proc.ImportFile(os.path.join(dir, f))
