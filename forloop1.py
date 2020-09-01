#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
my first for loop"""


# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]

# loop across the list vendors
for vendor in vendors:
    print(f"The approved creator of network gear is {vendor}")  # each time through the loop print value of x

print("\nOur loop has ended.")  # when the loop ends print this
