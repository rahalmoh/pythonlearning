
import os.path

def main():

    try:
    
        readfile=open("C:\\Users\\Mohamed\Desktop\\python learning\\bmw.txt", "r") # readlfile = variabe , "r" = read
        for line in readfile:
            print(line)
        readfile.close()
    except IOError:
            print("File not found")


# (try , except.) --> when trying to read a file, if not found, will print message instead crashing

main()