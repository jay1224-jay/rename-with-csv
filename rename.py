"""

this code will rename 
1301.txt -> j123259674.txt
1302.txt -> j758943745.txt
with csv and os.rename() 

"""

import csv
import os

with open('one.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile) # store data as dictionary type

    data = {}

    for row in spamreader: # store data to data(dict) because spamreader is not original dict type
        data[row['number']] = row['id']


for key in data.keys():
    try:
        os.rename(f"{key}.txt", f"{data[key]}.txt")
    except:
        print(f"{key}.txt is not exist")

print("\ndone\n")

