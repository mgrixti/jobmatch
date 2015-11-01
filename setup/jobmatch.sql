-- phpMyAdmin SQL Dump
-- version 4.4.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 30, 2015 at 04:50 AM
-- Server version: 5.6.25
-- PHP Version: 5.6.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jobmatch`
--

-- --------------------------------------------------------

--
-- Table structure for table `job_match`
--

CREATE TABLE IF NOT EXISTS `job_match` (
  `match_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `job_post`
--

CREATE TABLE IF NOT EXISTS `job_post` (
  `job_id` int(11) NOT NULL,
  `job_title` int(11) NOT NULL,
  `job_description` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `job_skill`
--

CREATE TABLE IF NOT EXISTS `job_skill` (
  `job_skill_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  `skill_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `skill`
--

CREATE TABLE IF NOT EXISTS `skill` (
  `skill_id` int(11) NOT NULL,
  `skill_name` varchar(30) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `skill`
--

INSERT INTO `skill` (`skill_id`, `skill_name`) VALUES
(1, 'Python'),
(2, 'Java'),
(3, 'Programming'),
(4, 'Database'),
(5, 'Unix'),
(6, 'Word'),
(7, 'Customer Service'),
(8, 'System Administration'),
(9, 'Office Administration'),
(10, 'Computer Security');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(20) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(20) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `first_name`, `last_name`) VALUES
(1, 'John', 'Doe');

-- --------------------------------------------------------

--
-- Table structure for table `user_skill`
--

CREATE TABLE IF NOT EXISTS `user_skill` (
  `user_skill_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `skill_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `job_skill`
--
ALTER TABLE `job_skill`
  ADD PRIMARY KEY (`job_skill_id`);

--
-- Indexes for table `skill`
--
ALTER TABLE `skill`
  ADD PRIMARY KEY (`skill_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `user_skill`
--
ALTER TABLE `user_skill`
  ADD PRIMARY KEY (`user_skill_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `job_skill`
--
ALTER TABLE `job_skill`
  MODIFY `job_skill_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `skill`
--
ALTER TABLE `skill`
  MODIFY `skill_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `user_skill`
--
ALTER TABLE `user_skill`
  MODIFY `user_skill_id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
