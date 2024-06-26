#!/usr/bin/python3
"""Program that lists all 'states' from the database 'hbtn_0e_0_usa'

Args:
    username: MySql server username
    password: User password
    db name: Name of the database
"""

import MySQLdb as msd
from sys import argv, exit


def main():
    """The main function so that the could doesn't run when imported
    """
    if len(argv) != 4:
        print(
                "usage: {} <mysql username> <mysql password> <database name>".
                format(argv[0])
            )
        exit(1)

    try:
        db = msd.connect(
                    host='localhost', port=3306, user=argv[1],
                    passwd=argv[2], db=argv[3]
                )
        cursor = db.cursor()
    except (msd.Error, msd.ProgrammingError) as e:
        try:
            print("MySQLdb Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQLdb Error: %s" % str(e))
        exit(2)

    try:
        cursor.execute(
                "SELECT * FROM states\
                        WHERE REGEXP_LIKE(name, '^N.*')\
                        ORDER BY id ASC"
            )
        states = cursor.fetchall()
    except (msd.Error, msd.ProgrammingError) as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))
        exit(3)

    for state in states:
        if state[1].startswith("N"):
            print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
