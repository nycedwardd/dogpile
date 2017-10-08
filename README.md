# Dogpile

Learning git. Writing sample code.

This is a repository for dumping code snippets that I've written that are mildly useful.

Thake what you need and have fun with it.

## bulk2.py
This script is an example of how to use Investigate's bulk api endpoint to retreive up to 1000 results with a single API call. This script will take an arbitrary list and chunk it up into 1000 element units, since the API takes a max of 1000 domains per call.

## reader.py

This is an example of reading in data from a CSV file and performing data enrichment on the data. It expects to store the results into an elastic search index.
