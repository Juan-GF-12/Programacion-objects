-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-12-2024 a las 08:30:44
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ecotech_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignaciones`
--

CREATE TABLE `asignaciones` (
  `id` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_proyecto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth`
--

CREATE TABLE `auth` (
  `id_auth` int(11) NOT NULL,
  `usuario` varchar(25) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `Rol` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `gerente` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`id`, `nombre`, `gerente`) VALUES
(1, 'RRHH', 'Juan garrido'),
(2, 'Recursos Humanos', 'Juan Pérez'),
(3, 'Tecnología', 'Ana Gómez'),
(4, 'Marketing', 'Carlos López'),
(5, 'Ventas', 'María Rodríguez'),
(6, 'Logística', 'Pedro Martínez'),
(7, 'Atención al Cliente', 'Laura Fernández'),
(8, 'Investigación y Desarrollo', 'Sofía Torres'),
(9, 'Finanzas', 'Luis García');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `id_departamento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id`, `nombre`, `direccion`, `telefono`, `email`, `fecha_inicio`, `salario`, `id_departamento`) VALUES
(1, 'esteban', 'garibaldi 01655', '984768894', 'esteban016@hotmail.com', '2003-09-29', 550000.00, NULL),
(2, 'Javier Morales', 'Calle 1, Ciudad A', '123456789', 'javier.morales@example.com', '2023-01-15', 35000.00, 1),
(3, 'Lucía Hernández', 'Calle 2, Ciudad B', '987654321', 'lucia.hernandez@example.com', '2022-12-01', 45000.00, 2),
(4, 'Roberto Sánchez', 'Calle 3, Ciudad C', '345678901', 'roberto.sanchez@example.com', '2023-05-20', 30000.00, 3),
(5, 'Isabel Romero', 'Calle 4, Ciudad D', '234567890', 'isabel.romero@example.com', '2023-03-18', 28000.00, 4),
(6, 'Fernando Castro', 'Calle 5, Ciudad E', '654321789', 'fernando.castro@example.com', '2023-06-12', 32000.00, 5),
(7, 'Carmen Méndez', 'Calle 6, Ciudad F', '123789456', 'carmen.mendez@example.com', '2022-10-10', 47000.00, 6),
(8, 'Alberto Ruiz', 'Calle 7, Ciudad G', '789123456', 'alberto.ruiz@example.com', '2023-02-25', 36000.00, 7),
(9, 'Marta Delgado', 'Calle 8, Ciudad H', '456789123', 'marta.delgado@example.com', '2023-07-01', 31000.00, 8),
(10, 'Sergio Ortega', 'Calle 9, Ciudad I', '678901234', 'sergio.ortega@example.com', '2023-04-05', 29000.00, 1),
(11, 'Patricia Navarro', 'Calle 10, Ciudad J', '567890123', 'patricia.navarro@example.com', '2022-11-25', 33000.00, 2),
(12, 'Diego Ríos', 'Calle 11, Ciudad K', '901234567', 'diego.rios@example.com', '2023-01-10', 35000.00, 3),
(13, 'Rocío León', 'Calle 12, Ciudad L', '890123456', 'rocio.leon@example.com', '2023-05-30', 38000.00, 4),
(14, 'Adrián Paredes', 'Calle 13, Ciudad M', '456123789', 'adrian.paredes@example.com', '2023-06-15', 30000.00, 5),
(15, 'María Esquivel', 'Calle 14, Ciudad N', '234890123', 'maria.esquivel@example.com', '2022-09-22', 40000.00, 6),
(16, 'Tomás Villalobos', 'Calle 15, Ciudad O', '345789123', 'tomas.villalobos@example.com', '2023-03-14', 37000.00, 7),
(17, 'Sofía Valencia', 'Calle 16, Ciudad P', '789456123', 'sofia.valencia@example.com', '2023-07-20', 42000.00, 8),
(18, 'Miguel Vega', 'Calle 17, Ciudad Q', '567123890', 'miguel.vega@example.com', '2023-01-25', 28000.00, 1),
(19, 'Silvia Franco', 'Calle 18, Ciudad R', '789234567', 'silvia.franco@example.com', '2023-06-01', 33000.00, 2),
(20, 'Alejandro Montero', 'Calle 19, Ciudad S', '456234789', 'alejandro.montero@example.com', '2022-12-05', 39000.00, 3),
(21, 'Laura Palacios', 'Calle 20, Ciudad T', '890456123', 'laura.palacios@example.com', '2023-05-12', 41000.00, 4),
(22, 'Pablo Castillo', 'Calle 21, Ciudad U', '234567891', 'pablo.castillo@example.com', '2023-03-10', 27000.00, 5),
(23, 'Ángela Medina', 'Calle 22, Ciudad V', '890345123', 'angela.medina@example.com', '2022-08-25', 44000.00, 6),
(24, 'Víctor Torres', 'Calle 23, Ciudad W', '567890234', 'victor.torres@example.com', '2023-04-18', 35000.00, 7),
(25, 'Julia Serrano', 'Calle 24, Ciudad X', '789567234', 'julia.serrano@example.com', '2023-06-22', 36000.00, 8),
(26, 'Carlos Fuentes', 'Calle 25, Ciudad Y', '678345789', 'carlos.fuentes@example.com', '2023-02-17', 40000.00, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `indicadores`
--

CREATE TABLE `indicadores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `valor` decimal(18,4) NOT NULL,
  `fecha_actualizacion` datetime NOT NULL,
  `fuente` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `indicadores`
--

INSERT INTO `indicadores` (`id`, `nombre`, `valor`, `fecha_actualizacion`, `fuente`) VALUES
(1, 'uf', 38374.6200, '2024-12-14 03:00:00', 'Mindicador.cl'),
(2, 'ivp', 39652.5200, '2024-12-14 03:00:00', 'Mindicador.cl'),
(3, 'euro', 1024.7600, '2024-12-13 03:00:00', 'Mindicador.cl'),
(4, 'dolar', 975.6700, '2024-12-13 03:00:00', 'Mindicador.cl'),
(5, 'uf', 38374.6200, '2024-12-14 03:00:00', 'Mindicador.cl'),
(6, 'uf', 38374.6200, '2024-12-14 03:00:00', 'Mindicador.cl'),
(7, 'uf', 38374.6200, '2024-12-14 03:00:00', 'Mindicador.cl'),
(8, 'uf', 38374.6200, '2024-12-14 03:00:00', 'Mindicador.cl');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectos`
--

CREATE TABLE `proyectos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proyectos`
--

INSERT INTO `proyectos` (`id`, `nombre`, `descripcion`, `fecha_inicio`) VALUES
(1, 'Optimización de Procesos', 'Mejorar los procesos internos de la empresa.', '2023-01-01'),
(2, 'Desarrollo de Software', 'Crear un sistema de gestión de inventario.', '2023-02-15'),
(3, 'Campaña Publicitaria', 'Lanzar una nueva campaña de marketing.', '2023-03-10'),
(4, 'Implementación de ERP', 'Integrar un sistema ERP en la organización.', '2023-04-20'),
(5, 'Automatización Logística', 'Automatizar las operaciones logísticas.', '2023-05-05');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_tiempo`
--

CREATE TABLE `registro_tiempo` (
  `id` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_proyecto` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `horas` decimal(5,2) NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registro_tiempo`
--

INSERT INTO `registro_tiempo` (`id`, `id_empleado`, `id_proyecto`, `fecha`, `horas`, `descripcion`) VALUES
(1, 1, 1, '2023-06-10', 8.00, 'Análisis de procesos existentes.'),
(2, 2, 2, '2023-06-12', 6.00, 'Diseño de interfaces para el sistema.'),
(3, 3, 3, '2023-06-15', 7.00, 'Planificación de la campaña publicitaria.'),
(4, 4, 4, '2023-06-18', 5.00, 'Configuración inicial del sistema ERP.'),
(5, 5, 5, '2023-06-20', 9.00, 'Automatización de tareas logísticas.'),
(6, 6, 2, '2023-06-25', 8.00, 'Pruebas del sistema desarrollado.');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignaciones`
--
ALTER TABLE `asignaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_empleado` (`id_empleado`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- Indices de la tabla `auth`
--
ALTER TABLE `auth`
  ADD PRIMARY KEY (`id_auth`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `id_departamento` (`id_departamento`);

--
-- Indices de la tabla `indicadores`
--
ALTER TABLE `indicadores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_empleado` (`id_empleado`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asignaciones`
--
ALTER TABLE `asignaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth`
--
ALTER TABLE `auth`
  MODIFY `id_auth` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `indicadores`
--
ALTER TABLE `indicadores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignaciones`
--
ALTER TABLE `asignaciones`
  ADD CONSTRAINT `asignaciones_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleados` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `asignaciones_ibfk_2` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`id_departamento`) REFERENCES `departamentos` (`id`) ON DELETE SET NULL;

--
-- Filtros para la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD CONSTRAINT `registro_tiempo_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleados` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `registro_tiempo_ibfk_2` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
