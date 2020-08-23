# search for string in a file and save in a file

import re

file = open("/Users/karpuri/Documents/Devnet/admin-tech/var/log/messages.2")

for x in file:
    if re.search("10ge0/0", x):
        save = open("/Users/karpuri/Documents/Devnet/save.txt", "a")
        save.write(x)
        save.close()
 file.close()
        
