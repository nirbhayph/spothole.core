-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: spothole
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `__authorities__`
--

DROP TABLE IF EXISTS `__authorities__`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `__authorities__` (
  `authority_id` varchar(50) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `photo_url` text NOT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`authority_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `__authorities__`
--

LOCK TABLES `__authorities__` WRITE;
/*!40000 ALTER TABLE `__authorities__` DISABLE KEYS */;
/*!40000 ALTER TABLE `__authorities__` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `__authority_zones__`
--

DROP TABLE IF EXISTS `__authority_zones__`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `__authority_zones__` (
  `authority_id` varchar(50) NOT NULL,
  `zipcode` varchar(10) NOT NULL,
  PRIMARY KEY (`authority_id`,`zipcode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `__authority_zones__`
--

LOCK TABLES `__authority_zones__` WRITE;
/*!40000 ALTER TABLE `__authority_zones__` DISABLE KEYS */;
/*!40000 ALTER TABLE `__authority_zones__` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `__public_users__`
--

DROP TABLE IF EXISTS `__public_users__`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `__public_users__` (
  `user_id` varchar(50) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `badge` varchar(100) NOT NULL,
  `photo_url` text NOT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `__public_users__`
--

LOCK TABLES `__public_users__` WRITE;
/*!40000 ALTER TABLE `__public_users__` DISABLE KEYS */;
/*!40000 ALTER TABLE `__public_users__` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `__report_comments__`
--

DROP TABLE IF EXISTS `__report_comments__`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `__report_comments__` (
  `user_type` varchar(50) NOT NULL,
  `comment_id` varchar(100) NOT NULL,
  `comment_text` text NOT NULL,
  `case_id` varchar(50) NOT NULL,
  `comment_date_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `__report_comments__`
--

LOCK TABLES `__report_comments__` WRITE;
/*!40000 ALTER TABLE `__report_comments__` DISABLE KEYS */;
/*!40000 ALTER TABLE `__report_comments__` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `__reports__`
--

DROP TABLE IF EXISTS `__reports__`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `__reports__` (
  `case_id` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `imageURL` text NOT NULL,
  `latitude` varchar(50) NOT NULL,
  `longitude` varchar(50) NOT NULL,
  `severity` int(2) NOT NULL,
  `userId` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_date` varchar(50) NOT NULL,
  `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `address` varchar(1000) DEFAULT NULL,
  `location_point` point DEFAULT NULL,
  PRIMARY KEY (`case_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `__reports__`
--

LOCK TABLES `__reports__` WRITE;
/*!40000 ALTER TABLE `__reports__` DISABLE KEYS */;
/*!40000 ALTER TABLE `__reports__` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-31 20:07:57
