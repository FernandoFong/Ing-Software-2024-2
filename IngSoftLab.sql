CREATE DATABASE lab_ing_software;

CREATE USER 'lab'@'localhost' IDENTIFIED BY 'Developer123!';

GRANT ALL PRIVILEGES ON lab_ing_software.* TO 'lab'@'localhost' WITH GRANT OPTION;

USE lab_ing_software;

CREATE TABLE `usuarios` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(500) DEFAULT NULL,
  `profilePicture` longblob,
  `superUser` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET='utf8mb4';

CREATE TABLE `peliculas` (
  `idPelicula` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `duracion` int DEFAULT NULL,
  `inventario` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`idPelicula`)
) ENGINE=InnoDB DEFAULT CHARSET='utf8mb4';

CREATE TABLE `rentar` (
  `idRentar` int NOT NULL AUTO_INCREMENT,
  `idUsuario` int NOT NULL,
  `idPelicula` int NOT NULL,
  `fecha_renta` datetime NOT NULL,
  `dias_de_renta` int DEFAULT '5',
  `estatus` tinyint DEFAULT '0',
  PRIMARY KEY (`idRentar`),
  KEY `idUsuario_idx` (`idUsuario`),
  KEY `idPelicula_idx` (`idPelicula`),
  CONSTRAINT `idPelicula` FOREIGN KEY (`idPelicula`) REFERENCES `peliculas` (`idPelicula`) ON DELETE CASCADE,
  CONSTRAINT `idUsuario` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 CHARSET='utf8mb4';
