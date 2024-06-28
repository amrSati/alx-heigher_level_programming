#!/usr/bin/python3
"""Prints all `City` objects from the given database
"""

from sys import argv, exit
from model_state import Base, State
from model_city import City
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

    cities_states = session.query(City, State).\
        filter(City.state_id == State.id).\
        order_by(City.id).all()

    for city, state in cities_states:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
