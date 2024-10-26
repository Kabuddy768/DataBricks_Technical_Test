# Write a query that will display the results below (Note: some columns might be renamed
# but use the column names above). It should only show 2020 data and order by driver
# points.

# Database Query for 2020 Data

import sqlite3

connection = sqlite3.connect('Join -Race Results')
cursor = connection.cursor()

query = """
SELECT * 
FROM drivers 
WHERE year = 2020
ORDER BY driver_points DESC;
"""

cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
connection.close()
