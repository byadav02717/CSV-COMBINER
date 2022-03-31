import sys

argc = len(sys.argv)
#variable to track if it is the first line of output
firstline = True
for i in range(1,argc):
    #spliting path into array. filename will be at last index
    pathname = sys.argv[i].split("/")
    filename = pathname[len(pathname)-1]

    #opeing file
    file = open(sys.argv[i], 'r')
    
    # reading first line
    line = file.readline()

    #printing first line
    if(firstline and line):
        print("{},{}".format(line.strip(), "\"filename\""))
        firstline = False
    #reading other lines in the file
    line = file.readline()
    while(line):
        print("{},\"{}\"".format(line.strip(), filename))
        line = file.readline()

    file.close()