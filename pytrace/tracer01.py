#!/usr/bin/python3
"""RZFeeser || Alta3 Research
Summary:
    Loop across all capture files within pcap/
    Looks for source / dest MACs within pcap/maclist.txt
    Results are stored in archive/{jobnum}/{macaddress}/
    
Updates to Make:
    Continue to make functions (some of these may be handeled better by scapy, not sure...)
    Add argparse
    Look at scapy.py library for detailed *pcap analysis
    """

import os
import uuid
from datetime import datetime
import pyshark
#import scapy # v heavy on memory, but good for small pcap analysis. Use tshark to reduce pcaps > use scapy to dig

# Open the file /pcaps/maclist.txt (list of macs to watch for)
def whatMacsAttack():
    """looks for the input file pcaps/maclist.txt and returns a dictionary with two lists"""
    with open("pcaps/maclist.txt") as maclist:
        perps = maclist.read().splitlines() # read the entire file into a single string, then split across "\n"
        maclist.seek(0) # move the cursor back to the start of the file (prevents having to close and reopen)
        shortenedperps = maclist.read().replace(":", "").splitlines() # strip out the : from the mac addresses
    return (perps, shortenedperps)  # this returns TWO values

# creates folders to store outputs in
def profilegenerator(shortperps, jobnum):
    for perp in shortperps:
        if not os.path.exists(f"archives/{jobnum}/{perp}"):
            os.makedirs(f"archives/{jobnum}/{perp}")
    return None

# define a function that can dynamically create filters
def filtergenerator():
    return None

# define a function that scrubs directories that contain pcaps with no packets (test by size?), or no pcaps
def cleanup():
    return None


def main():
    """pull together all of our functions into our trace program
    perps - ([mac list], [no colon mac list])
    movehere - directory location of our script
    jobnum - a unique string YYYY-MM-DD_HH-MM-SS used to create a folder to store the work
    """

    # returns two lists one with colons and one without
    perps = whatMacsAttack()     # returns a tuple ([mac list], [no colon mac list])

    # change to the real directory of where the script resides
    movehere = os.path.dirname(os.path.realpath(__file__))
    os.chdir(movehere) # changes our current working directory

    # create a YYYY-MM-DD_HH-MM-SS string
    jobnum = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    print(f"Profile reporting for this run available @ {movehere}archives/{jobnum}/")

    # create a series of user profiles
    profilegenerator(perps[1], jobnum)
      
    # obtain the list of input files to process
    for pcap in os.listdir("pcaps/"):
        # if a file is a network capture
        if pcap.endswith(".pcap") or pcap.endswith(".cap"):
            # then search that network capture for a "bad mac"
            for mac, sp in zip(perps[0], perps[1]):
                # create our displayfilter to pass to pyshark
                df = f"eth.dst=={mac} or eth.src=={mac}"
                # open a pcapfile, and apply our custom display filter
                cap = pyshark.FileCapture("pcaps/"+pcap, display_filter=df, output_file=f"archives/{jobnum}/{sp}/detection_report_for_{sp}.pcap")
                
                # this is REQUIRED for the "primed" cap object to run with the display filter
                cap.load_packets() # this line creates the output_file


main()
