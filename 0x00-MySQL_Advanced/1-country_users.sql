-- Creates a new table named 'users' to store unique user information
-- L5: Drops 'users' table if it exists to avoid conflicts.
-- L7: Primary key column for unique 'id', with auto-increment
-- L8 to L10: 'user' details, with country codes
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country CHAR(2) NOT NULL DEFAULT 'US' CHECK (country IN ('US', 'CO', 'TN'))
);
