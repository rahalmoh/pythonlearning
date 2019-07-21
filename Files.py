
import os.path

def main():
    out=open("C:\\Users\\Mohamed\Desktop\\python learning\\test.txt", "w") #out = variable , "r" = write
    out.write("Hello world\nhello")
    out.close()


    readfile=open("C:\\Users\\Mohamed\Desktop\\python learning\\test.txt", "r") # readlfile = variabe , "r" = read
    for line in readfile:
        print(line)
    readfile.close()
    
main()
