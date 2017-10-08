#!/usr/bin/python

"""Sample code to show using Investigate's the bulk API"""

#import fileinput
import json

import investigate


def chunk(dlist, listmax):
    """Function to take arbitrary lists and split them to chunks of 1000 max."""
    listmax = max(1, listmax)
    return [dlist[i:i + listmax] for i in range(0, len(dlist), listmax)]


# Read key, single line
with open('api-key.txt', 'r') as k:
    API_KEY = k.read().rstrip()
NEWDATA = {}
INV = investigate.Investigate(API_KEY)

# Initialize vars
i = 0
DOMAINS = {}

with open('topsites.txt') as f:
    DOMAINS = f.read().splitlines()

# How many chunks do we need?
SIZE = len(DOMAINS)
CHUNKS = SIZE / 1000
CHUNKS = chunk(DOMAINS, 1000)
print len(CHUNKS)
print len(CHUNKS[1])

for chunk in range(0, CHUNKS):
    # Call to Investigate bulk endpoint
    results = INV.categorization(CHUNKS[chunk], labels=True)
# pprint the results
    print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))
