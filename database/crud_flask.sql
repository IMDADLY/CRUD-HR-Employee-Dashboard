
-- Host: localhost
-- Generation Time: Jan 30, 2017 at 10:34 AM
-- Server version: 5.7.17-0ubuntu0.16.04.1
-- PHP Version: 7.0.13-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `crud_flask`
--

-- --------------------------------------------------------
12345123451234512345123451234512345123451234512345
Imran Abdul Rahiman
--
-- Table structure for table `phone_book`
--
CREATE TABLE `employee` (
  `id` varchar(5) NOT NULL PRIMARY KEY,
  `name` varchar(30) NOT NULL,
  `gender` ENUM('M', 'F', 'Other') NOT NULL,
  `salary` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `performance_score` varchar(3) NOT NULL,
  `remarks` varchar(100)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
--
-- Dumping data for table `phone_book`
--
INSERT INTO `employee` (`id`, `name`, `gender`, `salary`,`address`,`performance_score`,`remarks`) VALUES
(16, 'Henry Smith', 'M', '75000','Belmont Avenue','7.8','Very hardworking');
