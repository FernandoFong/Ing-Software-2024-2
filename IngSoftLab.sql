create database lab_ing_software;

create user 'lab'@'localhost' identified by 'Developer123!';

grant all privileges on lab_ing_software.* to 'lab'@'localhost'
with grant option;

use lab_ing_software;

CREATE TABLE `usuarios` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `apPat` varchar(200) NOT NULL,
  `apMat` varchar(200), 
  `password` varchar(64) NOT NULL,
  `email` varchar(500) DEFAULT NULL,
  `profilePicture` longblob,
  `superUser` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `peliculas` (
  `idPelicula` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `duracion` int DEFAULT NULL,
  `inventario` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`idPelicula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  CONSTRAINT `idPelicula` FOREIGN KEY (`idPelicula`) REFERENCES `peliculas` (`idPelicula`),
  CONSTRAINT `idUsuario` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
