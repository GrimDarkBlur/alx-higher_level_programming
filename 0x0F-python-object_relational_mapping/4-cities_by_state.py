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
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities on cities.state_id = states.id
ORDER BY cities.id
"""

if __name__ == "__main__":
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result)
