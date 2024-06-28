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
    if len(argv) != 5:
        print(
                "usage: {} <username> <password> <database> <state>".
                format(argv[0])
            )
        exit(1)

    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost:3306/{}'.
                    format(argv[1], argv[2], argv[3])
                )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
