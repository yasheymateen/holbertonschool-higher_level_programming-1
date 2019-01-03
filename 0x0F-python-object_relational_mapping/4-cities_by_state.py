#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, db_name = sys.argv[1:]
    cmd = """SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON state_id = states.id ORDER BY cities.id"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)

    cur = db.cursor()
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
