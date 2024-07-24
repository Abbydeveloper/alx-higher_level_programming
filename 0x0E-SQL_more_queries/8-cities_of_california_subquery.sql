--lists all Californian cities found in the database hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id = (SELECT id from states name = "California") Order by ID ASC;
