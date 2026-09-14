CREATE DATABASE IF NOT EXISTS prix_goncourt
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE prix_goncourt;


CREATE USER 'abinet002'@'localhost';
GRANT ALL PRIVILEGES ON prix_goncourt.* TO 'abinet002'@'localhost';
FLUSH PRIVILEGES;