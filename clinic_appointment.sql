-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 01:43 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinic_appointment`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient_data`
--

CREATE TABLE `patient_data` (
  `patient_name` char(30) NOT NULL,
  `patient_email` char(30) NOT NULL,
  `phone_num` int(11) NOT NULL,
  `date` char(30) NOT NULL,
  `patient_age` int(2) NOT NULL,
  `consultation_charge` char(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient_data`
--

INSERT INTO `patient_data` (`patient_name`, `patient_email`, `phone_num`, `date`, `patient_age`, `consultation_charge`) VALUES
('iman', 'iman@gm', 123546, '2023-11-4', 21, '144.0'),
('Adam', 'adam@gmail.com', 1234657, '2023-12-5', 31, '144.0'),
('Ian Ayres', 'ianayres@gmai.com', 126543875, '2023-07-21', 20, '171.0'),
('Ian Ayres', 'ianayres@gmail.com', 126543875, '2023-07-21', 20, '171.0'),
('Alaida Luana', 'alaida@gmail.com', 176015532, '2023-07-21', 50, '153.0');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
