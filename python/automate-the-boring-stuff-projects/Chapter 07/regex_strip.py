
import re

strip_regex = re.compile(r'\S+')

def strip_white_space(text):
    new_text = strip_regex.search(text)
    text = new_text.group(0)
    return text


print("Enter the text you would like stripped here:")
text = input()
print(strip_white_space(text))

