#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    r = r.json() # strip the json off of the response
    
    # create collection of cat facts
    listOfCatFacts = r.get("all")

    # pick ONE of the dictionaries from the collection of cat facts
    onefact = random.choice(listOfCatFacts)

    print(onefact.get("text"))


main()

