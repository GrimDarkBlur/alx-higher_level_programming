#!/usr/bin/env python3
"""
prints the contents of a database
using mysqldb
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    query = """
    SELECT id, name
    FROM states
    WHERE LEFT(name, 1) = "N"
    ORDER BY id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result)
