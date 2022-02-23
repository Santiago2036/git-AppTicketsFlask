-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-02-2022 a las 18:15:42
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tickets`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registrotiquetes`
--

CREATE TABLE `registrotiquetes` (
  `ID` int(11) NOT NULL,
  `USUARIO` varchar(25) NOT NULL,
  `fechaCreacion` date NOT NULL,
  `fechaActualizacion` date NOT NULL,
  `estatus` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `registrotiquetes`
--

INSERT INTO `registrotiquetes` (`ID`, `USUARIO`, `fechaCreacion`, `fechaActualizacion`, `estatus`) VALUES
(989766, 'Sebastian', '2015-02-11', '2019-02-19', 'cerrado'),
(1234567, 'diego', '2021-02-25', '2022-02-03', 'cerrado'),
(11111, 'mauro', '2022-02-01', '2022-02-03', 'abierto'),
(1088349398, 'santi', '2022-02-15', '2022-02-03', 'ABIERTO');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `registrotiquetes`
--
ALTER TABLE `registrotiquetes`
  ADD PRIMARY KEY (`fechaCreacion`,`fechaActualizacion`),
  ADD UNIQUE KEY `ID` (`ID`);
ALTER TABLE `registrotiquetes` ADD FULLTEXT KEY `USUARIO` (`USUARIO`);
ALTER TABLE `registrotiquetes` ADD FULLTEXT KEY `estatus` (`estatus`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
