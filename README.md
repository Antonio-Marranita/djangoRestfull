# djangoRestfull

Base de dados:
CREATE TABLE `post` (
  `idpost` int NOT NULL AUTO_INCREMENT,
  `author` varchar(100) NOT NULL,
  `datepost` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `text` varchar(1000) DEFAULT NULL,
  `active` tinyint DEFAULT '1',
  PRIMARY KEY (`idpost`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
