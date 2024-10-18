-- Create a table called users with unique constraints on email
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user, never null, auto increment, primary key
    email VARCHAR(255) NOT NULL UNIQUE,          -- Email must be unique and never null
    name VARCHAR(255)                            -- Name of the user, with a maximum of 255 characters
);
