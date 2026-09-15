CREATE DATABASE IF NOT EXISTS prix_goncourt
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE prix_goncourt;


CREATE USER 'abinet002'@'localhost';
GRANT ALL PRIVILEGES ON prix_goncourt.* TO 'abinet002'@'localhost';
FLUSH PRIVILEGES;


CREATE TABLE pg_person(
   p_ID_person INT,
   p_surname VARCHAR(30) NOT NULL,
   p_name VARCHAR(30) NOT NULL,
   p_age INT,
   PRIMARY KEY(p_ID_person)
);

CREATE TABLE pg_user(
   u_ID_user INT,
   u_email VARCHAR(75) NOT NULL,
   u_pasword VARCHAR(50) NOT NULL,
   u_statut VARCHAR(30),
   p_ID_person INT NOT NULL,
   PRIMARY KEY(u_ID_user),
   UNIQUE(p_ID_person),
   FOREIGN KEY(p_ID_person) REFERENCES pc_person(p_ID_person)
);

CREATE TABLE pg_membre(
   m_ID_membre INT,
   u_ID_user INT NOT NULL,
   PRIMARY KEY(m_ID_membre),
   UNIQUE(u_ID_user),
   FOREIGN KEY(u_ID_user) REFERENCES pc_user(u_ID_user)
);

CREATE TABLE pg_auteur(
   aut_ID_auteur INT,
   aut_bio TEXT,
   p_ID_person INT NOT NULL,
   PRIMARY KEY(aut_ID_auteur),
   UNIQUE(p_ID_person),
   FOREIGN KEY(p_ID_person) REFERENCES pc_person(p_ID_person)
);

CREATE TABLE pg_livre(
   l_ID_livre INT,
   l_id_auteur INT,
   l_tilte VARCHAR(50) NOT NULL,
   l_resume TEXT,
   l_pp VARCHAR(100),
   l_nb_pages INT,
   l_isbn BIGINT NOT NULL,
   l_price CURRENCY,
   aut_ID_auteur INT NOT NULL,
   PRIMARY KEY(l_ID_livre, l_id_auteur),
   UNIQUE(aut_ID_auteur),
   FOREIGN KEY(aut_ID_auteur) REFERENCES pc_auteur(aut_ID_auteur)
);

INSERT INTO pg_person (surname, name, age) VALUES
('Decoin', 'Didier', 81),
('Chandernagor', 'Francoise', 81),
('Jelloun', 'Tahar Ben', 81),
('Constant', 'Paul', 82),
('Claudel', 'Philippe', 64),
('Assouline', 'Pierre', 73),
('Schmitt', 'Eric-Emmanuel', 66),
('Laurens', 'Camille', 68),
('Bruckner', 'Pascal', 77),
('Angot', 'Christine', 67);

INSERT INTO pg_person (surname, name, age) VALUES
('Bergmann', 'Boris', 34),
('Chennevière', 'Louise', 39),
('Devi', 'Ananda', 69),
('Devillers', 'Sonia', 51),
('Godard', 'Anne', 55),
('Grondeau', 'Olivier', 49),
('Haenel', 'Yannick', 59),
('Hassaine', 'Lilia', 35),
('Jaenada', 'Philippe', 62),
('Jouannais', 'Jean-Yves', 62),
('Marsantes', 'Emma', 39),
('Mélois', 'Clémentine', 46),
('Orélien', 'Thélyson', 38),
('Prudhomme', 'Sylvain', 47),
('Rolin', 'Olivier', 79),
('Trigano', 'Patrice', 68);

