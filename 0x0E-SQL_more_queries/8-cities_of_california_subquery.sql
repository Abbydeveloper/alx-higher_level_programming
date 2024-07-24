--lists all Californian cities found in the database hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states name = "California") ORDER BY id ASC;
