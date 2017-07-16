#'U+{:04X}'.format(ord('云'))

import re
import codecs

data = ""
#MAC
#with open('input.txt', 'r',encoding='UTF-8') as f:
#Windows
with open('input.txt', 'r') as f:
    data = f.read()
    data = re.sub(r'<U\+(.{4})>',r'\\u\1',data)
    data = codecs.decode(data,"unicode_escape")

#python 2.7
#data = data.encode('UTF-8')
#with open('output.txt', mode='w+') as f:
#python 3.5
with open('output.txt',encoding='UTF-8', mode='w+') as f:
    f.write(data)

print("done")
