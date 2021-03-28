#!/usr/bin/env python3
"""
prints the contents of a database
using mysqldb
"""
import MySQLdb
import re
import sys


db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cursor = db.cursor()
query = """
SELECT cities.name
FROM states
INNER JOIN cities on cities.state_id = states.id
WHERE states.name = '{}'
ORDER BY cities.id
""".format(re.sub(r'(\n|\r|\x00|\\|\'|\"|\x1a)', r'\\\1', sys.argv[4]))

if __name__ == "__main__":
    cursor.execute(query)
    results = cursor.fetchall()
    for result in range(len(results) - 1):
        print(results[result][0],end=", ")
    print(results[-1][0])
