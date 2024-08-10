#File name: file_read_NayleneRondon.py
#Naylene Rondon
#4/10/17
#Syntax:file_variable.write (string)
#This program reads three line of data to a text file

def main():
    #Open a file
    infile = open("philosophers.txt", "r")  #The r is read mode

    #Read the file
    file_contents = infile.read()

    #Close file
    infile.close()

    #Print the data
    print(file_contents)

#Call main function

main()
