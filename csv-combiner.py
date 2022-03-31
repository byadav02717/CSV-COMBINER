import sys

argc = len(sys.argv)
firstline = True
for i in range(1,argc):
    pathname = sys.argv[i].split("/")
    filename = pathname[len(pathname)-1]
    file = open(sys.argv[i], 'r')
    line = file.readline()
    if(firstline):
        print("{},{}".format(line.strip(), "\"filename\""))
        firstline = False
    line = file.readline()
    while(line):
        print("{},\"{}\"".format(line.strip(), filename))
        line = file.readline()

    file.close()