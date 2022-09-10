#!/usr/bin/python3
"""
This module is about  a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa write one
that is safe from MySQL injections!
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    if len(argv) != 5:
        print("format is:0-select_states.py username password database state")
    else:
        list_dbparam = argv[1:]
        # Open database connection
        db = MySQLdb.connect(host='localhost', user=list_dbparam[0],
                             passwd=list_dbparam[1], db=list_dbparam[2],
                             port=3306)

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = """SELECT cities.name FROM cities
                 INNER JOIN states ON(states.id = cities.state_id)
                 WHERE states.name = %(name)s
                 ORDER BY cities.id ASC"""
        cursor.execute(sql, {'name': list_dbparam[3]})
        rows = cursor.fetchall()
        row_list = []
        for row in rows:
            row_list.append(row[0])
        print(", ".join(row_list))
        cursor.close()
        # disconnect from server
        db.close()
