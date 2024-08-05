-- Lists all cities in the database

SELECT cities.id, cities.name, states.name
FROM cities
	NATURAL JOIN states;
