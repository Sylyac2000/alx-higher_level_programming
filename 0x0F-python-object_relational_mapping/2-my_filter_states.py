#!/usr/bin/python3
"""
This module is about  a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    if len(argv) != 5:
        print("usage:2-my_filter_states.py username password database state")
    else:
        list_dbparam = argv[1:]
        # Open database connection
        db = MySQLdb.connect(host='localhost', user=list_dbparam[0],
                             passwd=list_dbparam[1], db=list_dbparam[2],
                             port=3306)

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = """SELECT * FROM states WHERE states.name LIKE '{0}'
                 ORDER BY states.id ASC""".format(list_dbparam[3])
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == list_dbparam[3]:
                print(row)

        # disconnect from server
        db.close()
