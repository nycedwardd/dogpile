#import fileinput
import investigate
import json
import csv
import time
from geoip import geolite2
from elasticsearch import Elasticsearch
from datetime import datetime
es = Elasticsearch()

infile = open('EXAMPLE.csv')
reader = csv.DictReader(infile)

# ignore 400 cause by IndexAlreadyExistsException when creating an index
#es.indices.create(index='csvdata', ignore=400)
es.indices.create(index='csvdata')
# Read key, single line
with open('api-key.txt', 'r') as k:
    api_key = k.read().rstrip()
inv = investigate.Investigate(api_key)

# Roll through
for row in reader:
    if row['cs_host'] != '':
        # printing row for diagnostic purposes so I know that script hasn't died
        print 'cs_host = ', row['cs_host']
        row['investigate'] = inv.security(row['cs_host'])
        row['domain_tags'] = inv.domain_tags(row['cs_host'])
        row['rr_dns_history'] = inv.rr_history(row['cs_host'])
        row['rr_ip_history'] = inv.rr_history(row['dst'])
        tmpcat = inv.categorization(row['cs_host'], labels=True)
        row['categorization'] = {}
        row['categorization']['security_status'] = tmpcat[row['cs_host']]['status']
        row['categorization']['security_categories'] = tmpcat[row['cs_host']
                                                              ]['security_categories']
        row['categorization']['content_categories'] = tmpcat[row['cs_host']
                                                             ]['content_categories']
        row['country'] = geolite2.lookup(row['dst']).country
        # cshost = {}
        # cshost['score'] =
    else:
        pass
    time.sleep(50.0 / 1000.0)
    es.index(index='csvdata', doc_type='EXAMPLE', body=row)
