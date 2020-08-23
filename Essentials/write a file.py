# If you want to wite a file then we have to open a file in WRITE access mode by using "w")
# Otherwise write() func will not work.
# if file doesnt exists it will create a new one

file = open("/Users/karpuri/Documents/Devnet/test1.txt","w")
file.write("I am writing the file")
file.close()

# To append text use "a"
file1 = open("/Users/karpuri/Documents/Devnet/test1.txt", "a")
file1.write("New line entry")
file1.close()

# view the file
file1 = open("/Users/karpuri/Documents/Devnet/test1.txt")
print(file1.read())
file1.close()
