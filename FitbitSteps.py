# Import packages
import json
import sqlite3
import os

# Connect to database
conn = sqlite3.connect('fitbitdb.sqlite')
cur = conn.cursor()

# Set up table
cur.executescript('''
DROP TABLE IF EXISTS Steps;

CREATE TABLE Steps (
    Date    TEXT NOT NULL PRIMARY KEY UNIQUE,
    Steps   Number
);
''')

# Show files in folder
filelist = os.listdir()
print(filelist)

#loop through files and add data to database
for i in filelist:
    if i.startswith("steps"): 
        fname = i

        str_data = open(fname).read()
        json_data = json.loads(str_data)

        for entry in json_data:
            x = entry.get("dateTime") 
            y = entry.get("value")

            cur.execute('''INSERT OR IGNORE INTO Steps (Date, Steps)
                VALUES ( ? , ? )''', (x, y) )

            conn.commit()
    else:
        continue
# Print Done! to show finished
print('Done!')
