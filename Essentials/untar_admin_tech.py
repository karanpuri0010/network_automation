#untar a file or admin tech

import tarfile
import os

file = tarfile.open('/Users/karpuri/Documents/Devnet/ATA/20190812-064347-admin-tech.tar.gz')

file.extractall("/Users/karpuri/Documents/Devnet/ATA/20190812-064347-admin-tech")

file.close()


