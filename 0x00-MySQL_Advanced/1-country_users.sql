-- Create a table called users with constraints, including country
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    email VARCHAR(255) NOT NULL UNIQUE,          -- Email must be unique and never null
    name VARCHAR(255),                           -- Name of the user
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US' -- Country enumeration with a default value of 'US'
);
