#!/usr/bin/python3
"""Program that lists all 'states' from the database 'hbtn_0e_0_usa'

Args:
    username: MySql server username
    password: User password
    db name: Name of the database
"""

import MySQLdb as msd
from sys import argv, exit
import re


def main():
    """The main function so that the could doesn't run when imported
    """
    if len(argv) != 5:
        print(
                "usage: {} <user> <password> <database> <state>".
                format(argv[0])
            )
        exit(1)

    if not re.search(r'[ \w]+', argv[4]):
        print('Error: Incorrect state input')
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
                        WHERE  BINARY name = {}".format(argv[4])
            )
        states = cursor.fetchall()
    except (msd.Error, msd.ProgrammingError) as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))
        exit(3)

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
