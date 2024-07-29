-- list all cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id=cities.states_id ORDER BY cities.id;
