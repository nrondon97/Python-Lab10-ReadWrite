#File name: file_write_NayleneRondon.py
#Naylene Rondon
#4/10/17
#Syntax:file_variable.write (string)
#This program writes three line of data to a text file

import winsound

def main():
    #Open a file
    outfile = open("philosophers.txt", "w")  #The w is write mode

    #Write the name of three philosphers
    outfile.write("Plato\n")
    outfile.write("Chardin\n")
    outfile.write("Buddha\n")

    #Close File
    outfile.close()
    print("Go to the folder and click on the text file.")

#Call main function

main()
