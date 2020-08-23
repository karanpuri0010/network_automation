# search for string in a file and save in a file

import re

file = open("/Users/karpuri/Documents/Devnet/ATA/20190812-064347-admin-tech/var/log/messages.2")

for x in file:
    if re.search("10ge0/0", x):
        save = open("/Users/karpuri/Documents/Devnet/ATA/save.txt", "a")
        save.write(x)
        save.close()
        
