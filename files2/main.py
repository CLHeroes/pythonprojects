import os
try:
    # if the file does not exist,
    # then it would throw an IOerror
    filename = 'Ziyo.txt'
    f = open(filename, 'rU')
    text = f.read()
    f.close()
    # Control jumps directly to here if the above
    # throws an error
except IOError:
    print("Problem reading: " + filename)
