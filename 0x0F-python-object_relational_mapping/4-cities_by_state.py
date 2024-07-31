#!/usr/bin/python3
"""  Lists Cities by States  """

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    db_cursor = db.cursor()
    db_cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                      cities INNER JOIN states on states.id=cities.states_id""")
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
    db_cursor.close()
    db.close()
