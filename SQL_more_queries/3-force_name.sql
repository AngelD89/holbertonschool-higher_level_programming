-- Script that creates the table force_name
-- The table has two columns: id and name (name cannot be NULL)

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
