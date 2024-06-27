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
    if len(argv) != 5:
        print(
                "usage: {} <user> <password> <database> <state>".
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
        cursor.execute("SELECT cities.name\
                FROM cities\
                JOIN states\
                WHERE cities.state_id = states.id and states.name = '{}'".
                format(argv[4]))
        cities = cursor.fetchall()
    except (msd.Error, msd.ProgrammingError) as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))
        exit(3)

    for i in range(len(cities)):
        if i and i <= len(cities) - 1:
            print(", ", end="")
        print(cities[i][0], end="")
    print()

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
