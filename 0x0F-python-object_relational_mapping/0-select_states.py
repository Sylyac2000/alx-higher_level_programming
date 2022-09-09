#!/usr/bin/python3
"""
This module is about listing all states from
a mysql database table called states
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

        sql = """SELECT * FROM states ORDER BY states.id ASC"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        

        # disconnect from server
        db.close()
