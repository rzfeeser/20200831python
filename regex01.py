#!/usr/bin/env python3

import urllib.request
import re

print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + "to search for the phrase:")
searchFor = input()
searchMe = urllib.request.urlopen(url).read().decode("utf-8")

result = re.search(searchFor, searchMe)

if result:
    print("Found a match!")
    print(dir(result))
    print(result)
    print(result.groups())
    print(result.group())
    print(result.start())
    print(result.span())
    print(searchMe[result.span()[0]: result.span()[1]+1000])
else:
    print("No match!")

