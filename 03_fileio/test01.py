#!/usr/bin/python3


if __name__=="__main__":
    # open file in read mode
    f = open("input01.txt", 'r')

    print("Content in the file:")
    for line in f:
        line = line.rstrip()
        print(line)

    f.close()

    # open file in append mode, use 'w' to overwrite file
    f = open("input01.txt", 'a')
    print("Appending new content to file...")
    f.write('C C C C\n')
    f.close()
