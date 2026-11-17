-- Makes first_table in the current schema, without failing if present
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
