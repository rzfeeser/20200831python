#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Prep for Tuesday / Review Monday"""

mypcap = {"packet1": "sip", "packet2": "http", "packet3": "http", "packet4": "tcp"}


def main():
    """code to search for a protocol within a 'trace'"""

    # ask user what protocol to search for
    protocoltosearchfor = input("What type of packet are you looking for\
 within the trace? ")


    print(mypcap.values())

    if protocoltosearchfor in mypcap.values():
        #print("TRUE! A packet of type " + protocoltosearchfor + " exists!")
        print(f"\nTRUE! At least one packet of type {protocoltosearchfor} exits!")
    else:
        print(f"\nFALSE! No packets of type {protocoltosearchfor} exist :(")


    print("\nThanks for using the packet analysis tool")

# Zach says this is best practice
if __name__ == "__main__":
    main()
