"""Find phone numbers an email addresses on the clipboard"""

import pyperclip, re

# Create phone regex.
phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?  # Area code
        (\s|-|\.)?  # Separator
        (\d{3})  # First 3 digits
        (\s|-|\.)  # Separator
        (\d{4})  # Last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))? #Extension
        )''', re.VERBOSE)

# Create email regex.
email_regex = re.compile(r'''(
        [a-zA-z0-9._%+-]+  # Username
        @  # @ symbol
        [a-zA-z0-9.-]+  # Domain name
        (\.[a-zA-Z]{2,4})  # Top-level domain
        )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
