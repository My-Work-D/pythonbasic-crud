
DROP DATABASE IF EXISTS user_data;

CREATE DATABASE IF NOT EXISTS  user_data;

SHOW DATABASES;

USE user_data;

CREATE TABLE users (
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       name VARCHAR(100),
                       age INT,
                       weight FLOAT
);
