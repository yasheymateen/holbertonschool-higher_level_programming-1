#!/usr/bin/python3
"""Script that lists all states with name starting with the uppercase letter N
Syntax: ./1-filter-states.py mysql-username mysql-password database-name
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, db_name = sys.argv[1:]
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
