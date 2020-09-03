#!/usr/bin/python3
"""RZFeeser || Alta3 Research
Loop across all capture files within a given directory"""

import os
import uuid
from datetime import datetime
import pyshark

def whatMacsAttack():
    """looks for the input file pcaps/maclist.txt and returns a dictionary with two lists"""
    with open("pcaps/maclist.txt") as maclist:
        perps = maclist.read().splitlines()
        maclist.seek(0)
        shortperps = maclist.read().replace(":", "").splitlines()
    return perps, shortperps

def profilegenerator(shortperps, jobnum):
    for perp in shortperps:
        if not os.path.exists(f"archives/{jobnum}/{perp}"):
            os.makedirs(f"archives/{jobnum}/{perp}")


def main():
    # returns two lists one with colons and one without
    perps, shortperps = whatMacsAttack()     # replaces --> perps = ["00:ca:fe:67:32:48", "68:bc:0c:7e:fc:bf"]

    # change to the real directory of where the script resides
    movehere = os.path.dirname(os.path.realpath(__file__))
    os.chdir(movehere) # changes our current working directory

    # create a YYYY-MM-DD_HH-MM-SS string
    jobnum = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    print(f"Profile reporting for this run available @ {movehere}archives/{jobnum}/")

    # create a series of user profiles
    profilegenerator(shortperps, jobnum)
    
    
    
    # obtain the list of input files to process
    for pcap in os.listdir("pcaps/"):
        # if a file is a network capture
        if pcap.endswith(".pcap") or pcap.endswith(".cap"):
            # then search that network capture for a "bad mac"
            for mac, sp in zip(perps, shortperps):
                # create our displayfilter to pass to pyshark
                df = f"eth.dst=={mac} or eth.src=={mac}"
                # open a pcapfile, and apply our custom display filter
                cap = pyshark.FileCapture("pcaps/"+pcap, display_filter=df, output_file=f"archives/{jobnum}/{sp}/detection_report_for_{sp}.pcap")
                
                # this is REQUIRED for the "primed" cap object to run with the display filter
                cap.load_packets() # this line creates the output_file


main()
