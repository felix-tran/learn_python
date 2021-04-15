# In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.

import re

# Your code goes here

sorted_dir_list = sorted(dir(re))
# print("\n".join(sorted_dir_list))

find_memebers = []

for member in sorted_dir_list:
    if "find" in member:
        find_memebers.append(member)

print("\n".join(find_memebers))