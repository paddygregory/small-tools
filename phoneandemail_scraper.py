#! python 3
# phoneandemail.py- finds phone numbers and email addresses on the clipboard
import pyperclip, re
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?             # area code; optional; 3 digits or (3 digits) and we backslash to escape the parentheses(so they're included)
    (\s|-|\.)?                     # separator
    (\d{3})                        # first 3 digits
    (\s|-|\.)?                     # separator
    (\d{4})                         # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension; some phone numbers have an extension 
    )''', re.VERBOSE)               # allows us to write regex in a readable format

emailReGex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.[a-zA-Z]{2,4}
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for group in emailReGex.findall(text):
    matches.append(group[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')