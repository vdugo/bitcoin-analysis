import csv

metadata_headers = []
metadata = []

with open('metadata.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    for index, row in enumerate(reader):
        if index == 0:
            metadata_headers = list(row)
        else:
            metadata.append(row)
            
for m in metadata:
    table_name = m[0]
    full_name = m[1]
    description = m[2]
    
    print(table_name)
    print(full_name)
    print(description)
    print()
