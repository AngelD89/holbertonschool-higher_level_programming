-- Script that create the table unique_id
-- id must be unique and have a default value of i

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
