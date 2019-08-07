# Usage: python3 regex_search.py regular_expression

import re, os

text_files = re.compile(r'[a-zA-Z0-9_]+.txt')
text_files = text_files.findall(' '.join(os.listdir('.')))

print("Enter a regular expression")
user_regex = re.compile(input())

for i in text_files:
    opened = open(i)
    fin_string = opened.read()
    final_ans = user_regex.findall(fin_string)
    print(final_ans)
