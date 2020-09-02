#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

from colorama import init
from termcolor import colored

import datagrabber

# use Colorama to make Termcolor work on Windows too
init()

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    """a function to perform fake commands on fake network devices"""
    for coffeetime in devicecmd.keys():
        print(colored('Handshaking. .. ... connecting with ', 'green', 'on_red') + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here




# start our main script
def main():
    """runtime code to teach about functions"""
    work2do = datagrabber.jsonreader()

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices





# call our main function
main()
