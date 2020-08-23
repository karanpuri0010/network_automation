# Step 1 open () function

## Below syntax has used open fuction to open a file in memory but u cannot view it.
## & while opening we need to store it in a variable inside memory

openit = open("/Users/karpuri/Downloads/var/log/vdebug")

# Step 2 read () function

## then to view strings inside file or read a file, u need to read it from memory, use read() function.
## we have stored that values inside new variable readit, so that we can print it later.

readit = openit.read()

# Step 3 print () function

## Once you read it u need to print it , so that user can view

print(readit)

#Step 4 close () function

## then you need to close that file , otherwise u know mem leak will happen :p
openit.close()



#Alternate way & easy way

file = open("/Users/karpuri/Downloads/var/tech/config")
print(file.read())
file.close()

# it has been noticed that you cannot use read(filename) or close(filename) as it doesnt recognize read as function similar to print() & open ().
