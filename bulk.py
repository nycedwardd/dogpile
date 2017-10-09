#!/usr/bin/python

"""Sample code to query the Investigate bulk api. Lists over 1000 will fail,
hitting the API maximum"""

# import fileinput
import json

import investigate

# Read key, single line
with open('api-key.txt', 'r') as k:
    API_KEY = k.read().rstrip()
NEWDATA = {}
INV = investigate.Investigate(API_KEY)

# Initialize vars
i = 0
DOMAINS = {}

with open('top1000.txt') as f:
    DOMAINS = f.read().splitlines()

RESULTS = INV.categorization(DOMAINS, labels=True)

# Pretty print the results
print json.dumps(RESULTS, sort_keys=True, indent=4, separators=(',', ': '))
