-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 03-10-2024 a las 22:26:10
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbtaller_mecanico`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reparaciones`
--

DROP TABLE IF EXISTS `reparaciones`;
CREATE TABLE IF NOT EXISTS `reparaciones` (
  `id_reparacion` int NOT NULL AUTO_INCREMENT,
  `matricula` varchar(20) NOT NULL,
  `id_pieza` int NOT NULL,
  `fecha_entrada` date NOT NULL,
  `fecha_salida` date NOT NULL,
  `cantidad` int NOT NULL,
  `problema` text NOT NULL,
  PRIMARY KEY (`id_reparacion`),
  UNIQUE KEY `id_reparacion` (`id_reparacion`,`matricula`,`id_pieza`),
  KEY `matricula` (`matricula`,`id_pieza`),
  KEY `id_pieza` (`id_pieza`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `reparaciones`
--

INSERT INTO `reparaciones` (`id_reparacion`, `matricula`, `id_pieza`, `fecha_entrada`, `fecha_salida`, `cantidad`, `problema`) VALUES
(7, 'XAW01', 2, '2024-02-12', '2024-04-12', 1, 'si'),
(10, 'XAW01', 2, '2024-12-11', '2024-12-12', 1, 'dfdsfdsa'),
(11, 'XAW02', 3, '2024-10-03', '2024-10-04', 50, 'fsafas');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `reparaciones`
--
ALTER TABLE `reparaciones`
  ADD CONSTRAINT `reparaciones_ibfk_1` FOREIGN KEY (`id_pieza`) REFERENCES `piezas` (`id_pieza`),
  ADD CONSTRAINT `reparaciones_ibfk_2` FOREIGN KEY (`matricula`) REFERENCES `vehiculos` (`matricula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
