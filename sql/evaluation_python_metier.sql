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

CREATE TABLE pg_livre (
    l_ID_livre INT PRIMARY KEY,
    l_ID_auteur INT NOT NULL,
    l_title VARCHAR(100) NOT NULL,
    l_resume TEXT,
    l_pp VARCHAR(255),
    l_nb_pages INT,
    l_isbn VARCHAR(13) NOT NULL UNIQUE,
    l_price DECIMAL(6, 2),
    FOREIGN KEY (l_ID_auteur)
        REFERENCES pg_auteur(aut_ID_auteur)
);

INSERT INTO pg_person (p_ID_person, p_surname, p_name, p_age) VALUES
(1,'Decoin', 'Didier', 81),
(2,'Chandernagor', 'Francoise', 81),
(3,'Jelloun', 'Tahar Ben', 81),
(4,'Constant', 'Paul', 82),
(5,'Claudel', 'Philippe', 64),
(6,'Assouline', 'Pierre', 73),
(7,'Schmitt', 'Eric-Emmanuel', 66),
(8,'Laurens', 'Camille', 68),
(9,'Bruckner', 'Pascal', 77),
(10,'Angot', 'Christine', 67);

INSERT INTO pg_user (u_ID_user, u_email, u_pasword, u_statut, p_ID_person) VALUES
(1, 'didier@goncourt.fr', '1234', 'President', 1),
(2, 'francoise@goncourt.fr', '1234', 'Member', 2),
(3, 'taharben@goncourt.fr', '1234', 'Member', 3),
(4, 'paul@goncourt.fr', '1234', 'Member', 4),
(5, 'philippe@goncourt.fr', '1234', 'Member', 5),
(6, 'pierre@goncourt.fr', '1234', 'Member', 6),
(7, 'eric@goncourt.fr', '1234', 'Member', 7),
(8, 'camille@goncourt.fr', '1234', 'Member', 8),
(9, 'pascal@goncourt.fr', '1234', 'Member', 9),
(10, 'christine@goncourt.fr', '1234', 'Member', 10);

INSERT INTO pg_membre (m_ID_membre, u_ID_user) VALUES
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 10);

INSERT INTO pg_person (p_ID_person, p_surname, p_name, p_age) VALUES
(11,'Bergmann', 'Boris', 34),
(12,'Chennevière', 'Louise', 39),
(13,'Devi', 'Ananda', 69),
(14,'Devillers', 'Sonia', 51),
(15,'Godard', 'Anne', 55),
(16,'Grondeau', 'Olivier', 49),
(17,'Haenel', 'Yannick', 59),
(18,'Hassaine', 'Lilia', 35),
(19,'Jaenada', 'Philippe', 62),
(20,'Jouannais', 'Jean-Yves', 62),
(21,'Marsantes', 'Emma', 39),
(22,'Mélois', 'Clémentine', 46),
(23,'Orélien', 'Thélyson', 38),
(24,'Prudhomme', 'Sylvain', 47),
(25,'Rolin', 'Olivier', 79),
(26,'Trigano', 'Patrice', 68);

INSERT INTO pg_auteur (aut_ID_auteur, aut_bio, p_ID_person) VALUES
(1,
 'Boris Bergmann est un écrivain français né en 1992 à Paris. Il publie son premier roman à 
  l''adolescence et développe une œuvre consacrée à la jeunesse, à l''identité et à la société contemporaine.',
 11),

(2,
 'Louise Chennevière est une écrivaine française. Elle est notamment l''autrice de Comme la 
 chienne, Mausolée et Pour Britney. Son œuvre interroge la condition féminine, la violence sociale et les relations familiales.',
 12),

(3,
 'Ananda Devi est une écrivaine mauricienne francophone née en 1957. Romancière, nouvelliste et 
 poétesse, elle construit une œuvre consacrée à l''identité, à la violence, à l''exclusion et à la société mauricienne.',
 13),

(4,
 'Sonia Devillers est une journaliste, animatrice de radio et écrivaine française née en 1975. 
 Dans ses livres, elle explore notamment la mémoire familiale, l''exil et l''histoire des Juifs de Roumanie.',
 14),

(5,
 'Anne Godard est une écrivaine française. Son travail littéraire explore l''intimité, les relations 
 familiales, le corps et les bouleversements qui traversent l''existence quotidienne.',
 15),

(6,
 'Olivier Grondeau est un écrivain français. Arrêté en Iran en 2022, il a été détenu pendant plus de 
 deux ans avant de revenir en France. Son écriture témoigne de l''enfermement, de la solitude et de la résistance.',
 16),

(7,
 'Yannick Haenel est un écrivain français né en 1967. Ancien professeur de français, il est notamment 
 l''auteur de Cercle, Jan Karski et Tiens ferme ta couronne.',
 17),

(8,
 'Lilia Hassaine est une journaliste et romancière française née en 1991. Elle est notamment l''autrice de
  L''Œil du paon, Soleil amer et Panorama. Ses romans examinent l''identité, les apparences et les transformations sociales.',
 18),

(9,
 'Philippe Jaenada est un écrivain français né en 1964. Il est connu pour ses enquêtes littéraires dans 
 lesquelles il revient sur des affaires criminelles et tente de restituer la vie de personnes oubliées.',
 19),

(10,
 'Jean-Yves Jouannais est un écrivain, critique d''art et commissaire d''exposition français né en 1964. 
 Ses travaux associent littérature, histoire de l''art, mémoire et réflexion sur la guerre.',
 20),

(11,
 'Emma Marsantes est une écrivaine française. Ses romans explorent les secrets familiaux, les traumatismes 
 transmis entre les générations et la manière dont les individus reconstruisent leur histoire.',
 21),

(12,
 'Clémentine Mélois est une artiste plasticienne, photographe et écrivaine française née en 1980. Membre de
  l''Oulipo, elle associe dans son travail la littérature, l''image, l''humour et les objets du quotidien.',
 22),

(13,
 'Thélyson Orélien est un poète, romancier et critique haïtien. Son œuvre est traversée par la mémoire, 
 l''exil, la violence politique et la recherche d''une appartenance.',
 23),

(14,
 'Sylvain Prudhomme est un écrivain français né en 1979. Voyageur et romancier, il s''intéresse aux territoires, 
 aux rencontres, à la nature et aux personnes qui vivent en marge.',
 24),

(15,
 'Olivier Rolin est un écrivain français né en 1947. Ancien militant politique, voyageur et reporter, il développe
  une œuvre marquée par l''histoire, les conflits, les paysages et la mémoire.',
 25),

(16,
 'Patrice Trigano est un écrivain, galeriste et spécialiste de l''art moderne. Ses livres mettent régulièrement 
 en scène des artistes et interrogent les liens entre création, histoire et justice.',
 26);

 INSERT INTO pg_livre (
    l_ID_livre,
    l_ID_auteur,
    l_title,
    l_resume,
    l_pp,
    l_nb_pages,
    l_isbn,
    l_price
)
VALUES
(
    1,
    11,
    'Minotaure',
    'À 23 ans, un jeune homme part à la rencontre de son père, qu''il n''a jamais connu, dans son cabinet de psychiatre.
     Ce récit autobiographique raconte sa quête familiale et rend hommage à sa mère.',
    'Le narrateur, son père, sa mère',
    256,
    '2226511873',
    20.90
),
(
    2,
    12,
    'Faire la peau',
    'À trente ans, une femme tente de se libérer de l''emprise de sa mère et d''une lignée familiale marquée par la violence. 
    Elle revisite son enfance et son adolescence afin de comprendre ce lien mêlant colère, amour et dépendance.',
    'La narratrice, sa mère',
    288,
    '2818063583',
    21.00
),
(
    3,
    13,
    'Chronique d''un royaume perdu',
    'Au Bouchon, un village isolé de l''île Maurice, quatre générations se succèdent depuis l''époque de l''esclavage. 
    Un enfant devient le chroniqueur de ce royaume afin d''en conserver les luttes, les amours et la mémoire.',
    'Le chroniqueur, les habitants du Bouchon',
    464,
    '2246846943',
    24.00
),
(
    4,
    14,
    'Le fabuleux piano',
    'Sonia Devillers recherche un piano à queue volé à une famille juive par les nazis en 1943. 
    Son enquête sur les instruments pillés pendant l''Occupation fait résonner l''histoire collective avec celle de sa propre grand-mère.',
    'La narratrice, sa grand-mère, les propriétaires du piano',
    288,
    '2221286804',
    21.00
),
(
    5,
    15,
    'Nous aussi',
    'Un récit consacré à des personnages confrontés à leur histoire intime et familiale. 
    Le roman examine ce qui rapproche les êtres, mais également les silences et les blessures qui les séparent.',
    'La narratrice, sa famille',
    192,
    '2330225571',
    20.00
),
(
    6,
    16,
    'Joseph dans la nuit',
    'À travers le personnage de Joseph, le récit évoque l''enfermement, la nuit carcérale et les pensées qui permettent de résister. 
    Le protagoniste tente de préserver son identité malgré l''isolement et l''incertitude.',
    'Joseph, ses proches, ses gardiens',
    224,
    '237880492X',
    19.90
),
(
    7,
    17,
    'La solitude des professeurs est infinie',
    'Un professeur observe la transformation de son métier et la manière dont l''école est considérée par la société. 
    Le roman aborde la transmission, la vocation d''enseigner et la solitude ressentie face aux difficultés du système scolaire.',
    'Le professeur, ses élèves, ses collègues',
    320,
    '2073101542',
    21.50
),
(
    8,
    18,
    'Je',
    'Le roman redonne une voix à une femme jusque-là enfermée dans le regard et le récit des autres. 
    Elle raconte son existence à la première personne et tente de reprendre possession de son identité.',
    'La narratrice',
    256,
    '2073099947',
    20.50
),
(
    9,
    19,
    'L''inconnue du quai de Javel',
    'Philippe Jaenada enquête sur une jeune femme retrouvée morte près du quai de Javel.
     À partir des archives disponibles, il cherche à reconstruire son identité, son parcours et les circonstances de sa disparition.',
    'La jeune inconnue, le narrateur, les enquêteurs',
    528,
    '2080490893',
    24.00
),
(
    10,
    20,
    'Une forêt',
    'Le narrateur traverse une forêt réelle et mentale dans laquelle les souvenirs, les œuvres et les événements historiques se répondent.
     Le paysage devient progressivement un espace de mémoire et de réflexion.',
    'Le narrateur',
    112,
    '2226499520',
    17.90
),
(
    11,
    21,
    'N''efface pas mes cercles',
    'En 1980, une femme se suicide dans un appartement. Le roman remonte le temps pour comprendre son histoire, son mariage dans les années 1950 et 
    les destins brisés qui ont marqué plusieurs générations.',
    'La femme, son mari, leur famille',
    160,
    '2378562950',
    19.50
),
(
    12,
    22,
    'Choses que je croyais perdues',
    'Alors qu''Émilie prépare son déménagement, les objets qu''elle retrouve font réapparaître des souvenirs qu''elle pensait disparus. 
    Chaque chose devient le point de départ d''une évocation intime, drôle ou mélancolique.',
    'Émilie, ses proches',
    176,
    '2073112641',
    19.50
),
(
    13,
    23,
    'C''était ça ou mourir',
    'Après l''embrasement de son quartier de Port-au-Prince, Jonas Dorléon quitte Haïti avec un diplôme, un cahier de poèmes et une photographie de sa mère. 
    Le roman raconte son exil et sa lutte pour reconstruire sa vie.',
    'Jonas Dorléon, sa mère',
    272,
    '2246847060',
    21.60
),
(
    14,
    24,
    'De l''autre côté du lac',
    'Près d''un lac de haute montagne, Paola, une photographe accompagnant des chercheurs, aperçoit quelque chose sur un versant. 
    Après la découverte d''un corps, elle décide de rester seule dans la réserve avant de disparaître.',
    'Paola, le narrateur, les chercheurs',
    288,
    '2707358231',
    22.00
),
(
    15,
    25,
    'La Guerre éternelle',
    'À partir de voyages, de souvenirs et de conflits anciens ou contemporains, le narrateur réfléchit à la permanence de la guerre dans
     l''histoire humaine et aux traces qu''elle laisse dans les paysages et les mémoires.',
    'Le narrateur, les soldats, les témoins',
    352,
    '2073100678',
    22.50
),
(
    16,
    26,
    'Bataille au procès',
    'En 1956, Georges Bataille doit répondre de son œuvre devant la justice. Le roman met en scène le procès, les débats autour de la
     liberté littéraire et l''affrontement entre création artistique et morale publique.',
    'Georges Bataille, les magistrats, les témoins',
    192,
    '2862313599',
    19.00
);