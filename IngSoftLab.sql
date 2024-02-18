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

-- Insertar registros en la tabla usuarios
INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser)
VALUES 
('Juan', 'García', 'López', 'password123', 'juan@example.com', 1),
('María', 'Martínez', 'Gómez', 'securepass', 'maria@example.com', 0),
('Carlos', 'Hernández', 'Pérez', '123456', 'carlos@example.com', 0),
('Laura', 'Díaz', 'Rodríguez', 'laurapass', 'laura@example.com', 0),
('Pedro', 'Sánchez', 'López', 'peterpass', 'pedro@example.com', 0);

SELECT * FROM usuarios;

INSERT INTO peliculas (nombre, genero, duracion, inventario)
VALUES 
('Pelicula1', 'Acción', 120, 10),
('Pelicula2', 'Comedia', 90, 15),
('Pelicula3', 'Drama', 110, 20),
('Pelicula4', 'Ciencia Ficción', 150, 8),
('Pelicula5', 'Romance', 100, 12);

SELECT * FROM peliculas;


-- Insertar registros en la tabla rentar
INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus)
VALUES 
(13, 1, '2024-02-17 12:00:00', 3, 1),
(15, 3, '2024-02-16 10:30:00', 5, 0),
(13, 2, '2024-02-15 08:45:00', 7, 1),
(16, 5, '2024-02-14 14:20:00', 4, 1),
(14, 4, '2024-02-13 16:00:00', 2, 0);

SELECT * FROM rentar;

DELETE  FROM usuarios;
DELETE FROM rentar;
DELETE FROM peliculas;