#untar a file or admin tech

import tarfile
import os

file = tarfile.open('/Users/karpuri/Documents/Devnet/admin-tech.tar.gz')

file.extractall("/Users/karpuri/Documents/Devnet/admin-tech")

file.close()
