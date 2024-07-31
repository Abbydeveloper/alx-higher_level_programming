#!/usr/bin/python3
""" Safe state filter """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    db_cursor = db.cursor()
    match = sys.argv[4]
    db_cursor.execute("SELECT * FROM states WHERE name like %s", (match, ))
    rows = db.fetchall()
    for row in rows:
        print(row)
    db_curser.close()
    db.close()
