#!/usr/bin/python3
"""  Lists Cities by States  """

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    db_cursor = db.cursor()
    match = sys.argv[4]
    db_cursor.execute("""SELECT cities.name FROM cities INNER JOIN states ON
                      states.id=cities.state_id
                      WHERE states.name=%s""", (match, ))
    rows = db_cursor.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    db_cursor.close()
    db.close()
