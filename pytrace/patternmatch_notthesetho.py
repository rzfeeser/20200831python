#!/usr/bin/env python3
#Author: RZFeeser RZFeeser@alta3.com

"""Script to search for a pattern match"""

import argparse
import os # used to walk the system
import fnmatch # for regex pattern matching

EXCLUDE = ["/usr", "/home", "/var"] ## Dont search in these locations


def find(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] # remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files: # always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name.lower(), pattern): # if match
                result.append(os.path.join(root, name)) # add to our list
    return result # return the list

def main():
    """runtime code"""
    #lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    #lookfor = lookfor.lower()
    lookfor = args.lookfor
    lookwhere = args.lookwhere


    print("Results: ", find(lookfor, lookwhere)) # call function


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search for files within the system. Does not look in /usr /home or /var.')
    parser.add_argument('-f', '--lookfor', help='This is what to search for. Example: "*.py"')
    parser.add_argument('-w', '--lookwhere', default="/home/student/", help='This is the location to search. Example: "/var"')

    args = parser.parse_args()
    main()
