#!/usr/bin/python

"""Read in data from a csv file and store enriched results within ElasticSearch"""
# import json
import csv
import time

#import fileinput
import investigate
from elasticsearch import Elasticsearch

# from datetime import datetime
ES = Elasticsearch()

INFILE = open('EXAMPLE.csv')
READER = csv.DictReader(INFILE)

# ignore 400 cause by IndexAlreadyExistsException when creating an index
#es.indices.create(index='csvdata', ignore=400)
ES.indices.create(index='csvdata')
# Read key, single line
with open('api-key.txt', 'r') as k:
    API_KEY = k.read().rstrip()
INV = investigate.Investigate(API_KEY)

# Roll through
for row in READER:
    if row['cs_host'] != '':
        # printing row for diagnostic purposes so I know that script hasn't died
        print 'cs_host = ', row['cs_host']
        row['investigate'] = INV.security(row['cs_host'])
        row['domain_tags'] = INV.domain_tags(row['cs_host'])
        row['rr_dns_history'] = INV.rr_history(row['cs_host'])
        row['rr_ip_history'] = INV.rr_history(row['dst'])
        tmpcat = INV.categorization(row['cs_host'], labels=True)
        row['categorization'] = {}
        row['categorization']['security_status'] = tmpcat[row['cs_host']]['status']
        row['categorization']['security_categories'] = tmpcat[row['cs_host']
                                                             ]['security_categories']
        row['categorization']['content_categories'] = tmpcat[row['cs_host']
                                                            ]['content_categories']
        # row['country'] = geolite2.lookup(row['dst']).country
        # cshost = {}
        # cshost['score'] =
    else:
        pass
    time.sleep(50.0 / 1000.0)
    ES.index(index='csvdata', doc_type='EXAMPLE', body=row)
