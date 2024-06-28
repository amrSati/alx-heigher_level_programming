#!/usr/bin/python3
"""Script that lists all `State` objects from the database `hbtn_0e_6_usa`
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """main function so that the code doesn't run when imported
    """
    if len(argv) != 4:
        print("usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost:3306/{}'.
                    format(argv[1], argv[2], argv[3])
                )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        print(f"{state.id}: {state.name}")

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
