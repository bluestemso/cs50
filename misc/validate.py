import re

email = input("What's your email? ").strip()

if re.search(r'^(\w|\.)+@(\w+\.)?\w+\.edu$', email, re.IGNORECASE):
    print('yeah thats it')
else:
    print('nope\nnope\nnope')

