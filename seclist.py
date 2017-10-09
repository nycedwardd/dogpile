#!/usr/bin/python

"""Sample code to read in from a text file and perform data enrichment.
Results are dumped as a csv file"""
#import csv
#import fileinput
#import json
import sys
#import time
#from datetime import datetime

import investigate

# Read key, single line
with open('api-key.txt', 'r') as k:
    API_KEY = k.read().rstrip()
INV = investigate.Investigate(API_KEY)

# Check to see if we have a parameter passed
# Should be the file name to read
if len(sys.argv) > 1:
    DLIST = sys.argv[1]
else:
    print "Must provide a domain list. Defaulting to seclist.txt"
    DLIST = "seclist.txt"
    # exit()

# Get domain list into domains[]
DOMAINS = []
with open(DLIST, 'r') as d:
    DOMAINS = d.readlines()

print "Domain,Content Category, Security Category"
# If the domain has samples associated with it, print out that domain
for domain in DOMAINS:
    result = INV.categorization(domain.rstrip(), labels=True)
    msg1 = ",", result[domain.rstrip()]['content_categories'], ","
    msg2 = result[domain.rstrip()]['security_categories']
    print domain.rstrip(), msg1, msg2
