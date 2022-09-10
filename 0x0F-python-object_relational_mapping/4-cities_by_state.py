#!/usr/bin/python3
"""
This module is about a script that lists
all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    if len(argv) != 4:
        print("format is:0-select_states.py username password database")
    else:
        list_dbparam = argv[1:]
        # Open database connection
        db = MySQLdb.connect(host='localhost', user=list_dbparam[0],
                             passwd=list_dbparam[1], db=list_dbparam[2],
                             port=3306)

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = """SELECT cities.id, cities.name, states.name FROM cities
                 INNER JOIN states ON(states.id = cities.state_id)
                 ORDER BY cities.id ASC"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # disconnect from server
        db.close()
