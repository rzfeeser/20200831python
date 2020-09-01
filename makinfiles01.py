#!/usr/bin/python3
"""RZFeeser | Alta3 Research
File examples"""

def main():

    # this is the lame way you should understand but prob. never do...
    myfile = open("instr.txt", "w") # w means write or "create a brand new file"
    myfile.write("I can write whatever i want into the file\n")
    myfile.write("This will be on the second line\n")
    # everyone forgets to do this...
    myfile.close()  # this closes the file, and removes the object "myfile"


    # this is the new "cool" way to work with files
    with open("instr2.txt", "w") as myfile:
        myfile.write("I can write whatever i want into the file\n")
        myfile.write("This will be on the second line\n")
        myfile.write("This will be a UNIQUE 3rd line!")

    # uncomment this line to throw an I/O error on a CLOSED file
    #myfile.write("this will cause an error")

    # open the file we just made (instr2.txt) in READ mode
    with open("instr2.txt", "r") as scoobydoo:
        listoflines = scoobydoo.readlines()
        print(listoflines)

if __name__ == "__main__":
    main()
