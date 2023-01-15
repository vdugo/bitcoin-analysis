import csv

import nasdaqdatalink

# All of the table names that we want
TABLE_NAMES = [
    'ATRCT', 
    'AVBLS', 
    'BLCHS', 
    'CPTRA', 
    'CPTRV', 
    'DIFF', 
    'ETRAV', 
    'ETRVU', 
    'HRATE', 
    'MIREV', 
    'MKPRU', 
    'MKTCP', 
    'NADDU', 
    'NTRAN', 
    'NTRAT', 
    'NTRBL', 
    'NTREP', 
    'TOTBC', 
    'TOUTV', 
    'TRFEE', 
    'TRFUS', 
    'TRVOU'
]
# The metadata for each table as a list of string 5-tuples
metadata: list[tuple[str, str, str, str, str]] = []
# read our nasdaq api key from the local file
nasdaqdatalink.read_key('.bitcoinnasdaqapikey')
# for each table name, download the corresponding table dataset from nasdaq
# write each dataset to a csv in our local directory with the same name as
# the table name
# also, retrieve the metadata that we want from the same dataset and append an
# entry to our list of string 5-tuples
for table_name in TABLE_NAMES:
    data = nasdaqdatalink.get(f'BCHAIN/{table_name}')
    data.to_csv(f'{table_name}.csv')
    
    met = nasdaqdatalink.Dataset(f'BCHAIN/{table_name}')
    metadata.append( (table_name, met.name, met.description, met.newest_available_date, met.oldest_available_date) )

# now write our metadata to a local csv file called 'metadata.csv'
with open('metadata.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    # write the headers as the first row in the csv file
    writer.writerow(['TableName', 'FullName', 'Description', 'NewestAvailableDate', 'OldestAvailableDate'])
    # write the rest of the rows from the metadata list
    for m in metadata:
        writer.writerow(list(m))
