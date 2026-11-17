-- Makes unique_id where the id field defaults to 1 and must be distinct
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
