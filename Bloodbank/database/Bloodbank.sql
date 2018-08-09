-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 09, 2018 at 12:16 PM
-- Server version: 5.7.23-0ubuntu0.16.04.1
-- PHP Version: 7.0.30-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Bloodbank`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `uid` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Age` int(2) NOT NULL,
  `Gender` enum('M','F') NOT NULL,
  `BloodGroup` enum('A+','A-','B+','B-','O+','O-','AB+','AB-') NOT NULL,
  `District` varchar(20) NOT NULL,
  `State` varchar(20) NOT NULL,
  `PhoneNumber` bigint(10) NOT NULL,
  `Donor` tinyint(1) NOT NULL DEFAULT '0',
  `Password` char(32) DEFAULT NULL,
  `Username` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`uid`, `Name`, `Age`, `Gender`, `BloodGroup`, `District`, `State`, `PhoneNumber`, `Donor`, `Password`, `Username`) VALUES
(1, 'Midhun', 32, 'M', 'A+', 'Mumbai', 'Maharashtra', 7354919826, 1, 'abcd', 'midhun01'),
(2, 'Chithra', 23, 'F', 'O+', 'Kozhikode', 'Kerala', 9895982453, 1, NULL, NULL),
(3, 'Aswin', 29, 'M', 'AB+', 'Erode', 'TamilNadu', 9125475355, 0, NULL, NULL),
(4, 'Varun', 26, 'M', 'A-', 'Palakkad', 'Kerala', 9854536542, 0, NULL, NULL),
(5, 'Veena', 44, 'F', 'A-', 'Kolkata', 'Bengal', 9854989890, 1, NULL, NULL),
(9, 'Deepak', 34, 'M', 'O-', 'Bengaluru', 'Karnataka', 8712664327, 1, NULL, NULL),
(13, 'Shamna', 22, 'F', 'B+', 'Ahmedabad', 'Gujrat', 8426567234, 0, NULL, NULL),
(14, 'Aparna', 29, 'F', 'B-', 'Ahmedabad', 'Gujrat', 9034353484, 1, NULL, 'aparnaap');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`uid`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
