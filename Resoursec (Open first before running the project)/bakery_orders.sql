-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 01, 2021 at 01:56 PM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bakery_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `bakery_orders`
--

CREATE TABLE IF NOT EXISTS `bakery_orders` (
`Order_id` int(11) NOT NULL,
  `full_name` varchar(50) NOT NULL,
  `mobile_no` bigint(10) NOT NULL,
  `order_items` varchar(200) NOT NULL,
  `order_quantities` varchar(200) NOT NULL,
  `pickup_order_date` varchar(12) NOT NULL,
  `pickup_order_time` varchar(10) NOT NULL,
  `payment_method` varchar(20) NOT NULL,
  `payment_made` int(255) NOT NULL,
  `total_price` int(255) NOT NULL,
  `return_amount` int(255) NOT NULL,
  `order_date` varchar(20) NOT NULL,
  `order_time` varchar(20) NOT NULL,
  `Country_code` varchar(10) NOT NULL DEFAULT '+91'
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bakery_orders`
--

INSERT INTO `bakery_orders` (`Order_id`, `full_name`, `mobile_no`, `order_items`, `order_quantities`, `pickup_order_date`, `pickup_order_time`, `payment_method`, `payment_made`, `total_price`, `return_amount`, `order_date`, `order_time`, `Country_code`) VALUES
(6, 'Rohit Chaurasia', 8756436112, 'Pastry', '20', '1/07/2021', '', 'Cash', 1500, 1000, 500, '2021-07-01', '13:38:51.233843', '+91'),
(7, 'Rohit Chaurasia', 8756436112, 'Biscuit', '3', '1/07/2021', '', 'Cash', 2500, 900, 1600, '2021-07-01', '13:40:09.554647', '+91'),
(8, 'Rohit Chaurasia', 8756436112, 'Pastry, Biscuit', '3, 2', '1/07/2021', '', 'Cash', 6000, 750, 5250, '2021-07-01', '13:48:53.376832', '+91'),
(9, 'Rohit Chaurasia', 8756436112, 'Pastry', '10', '1/07/2021', '', 'Cash', 6000, 500, 5500, '2021-07-01', '13:54:19.343614', '+91'),
(10, 'Rohit Chaurasia', 8756436112, 'Biscuit, Pastry', '2, 10', '1/07/2021', '', 'Cash', 5000, 1100, 3900, '2021-07-01', '13:59:41.484571', '+91'),
(11, 'Rohit Chaurasia', 8756436112, 'Biscuit, Pastry', '2, 10', '1/07/2021', '', 'Cash', 5000, 1100, 3900, '2021-07-01', '16:55:50.510922', '+91'),
(12, 'Rohit Chaurasia', 8756436112, 'Biscuit, Pastry', '2, 10', '1/07/2021', '', 'Cash', 5000, 1100, 3900, '2021-07-01', '16:57:31.231486', '+91'),
(13, 'Rohit Chaurasia', 8756436112, 'Biscuit, Pastry', '2, 10', '1/07/2021', '', 'Cash', 5000, 1100, 3900, '2021-07-01', '16:58:27.956513', '+91');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bakery_orders`
--
ALTER TABLE `bakery_orders`
 ADD PRIMARY KEY (`Order_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bakery_orders`
--
ALTER TABLE `bakery_orders`
MODIFY `Order_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=14;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
