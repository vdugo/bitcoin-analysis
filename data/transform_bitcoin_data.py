import csv

import pandas as pd

metadata_headers = []
metadata = []

with open('metadata.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    for index, row in enumerate(reader):
        if index == 0:
            metadata_headers = list(row)
        else:
            metadata.append(row)

# there are some csv files with a January 2nd 2009 date, use one
# of them to initialize our new dataframe's indexes as the dates from
# January 2nd 2009 to present (Dec 6, 2022).
avbls_df = pd.read_csv('avbls.csv')

bitcoin_df = pd.DataFrame(index=avbls_df['Date'])

# combine all the tables into a single pandas dataframe
# the index will be the dates, since all the dates are the same
# from January 3rd 2009 to present (besides a few January 2nd 2009).
# for each table, make its table name a column in our new
# dataframe, then make the old `Value` column our new values
# for each respective table
for m in metadata:
    table_name = m[0]
    
    current_df = pd.read_csv(f'{table_name}.csv', index_col='Date')
    bitcoin_df[table_name] = current_df['Value']

# write the new csv to a bitcoin.csv file
bitcoin_df.to_csv('bitcoin.csv')
    