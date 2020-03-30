-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: customer
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookingdetails`
--

DROP TABLE IF EXISTS `bookingdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bookingdetails` (
  `username` varchar(10) DEFAULT NULL,
  `Name` varchar(15) NOT NULL,
  `Bookingid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Address` varchar(45) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Adharcard` varchar(20) NOT NULL,
  `Contact` varchar(10) NOT NULL,
  `CarNo` varchar(45) NOT NULL,
  `CarBrand` varchar(10) NOT NULL,
  `CarModel` varchar(45) NOT NULL,
  `Carcolour` varchar(45) NOT NULL,
  `Slotno` varchar(45) NOT NULL,
  `Date` varchar(50) NOT NULL,
  `Time` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Bookingid`),
  KEY `username` (`username`),
  KEY `Bookingid` (`Bookingid`),
  CONSTRAINT `bookingdetails_ibfk_1` FOREIGN KEY (`username`) REFERENCES `login` (`username`),
  CONSTRAINT `bookingdetails_ibfk_2` FOREIGN KEY (`username`) REFERENCES `login` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=1046 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookingdetails`
--

LOCK TABLES `bookingdetails` WRITE;
/*!40000 ALTER TABLE `bookingdetails` DISABLE KEYS */;
INSERT INTO `bookingdetails` VALUES ('shreyanshu','qws',1027,'swq','Male','ws','swq','wsq','TESLA','wwq','ws','b5','2019, 4, 4','10am'),('gauri','gauri',1029,'thane','Female','1111','1111','111','LANDROVER','111','111','b1','2019, 4, 4','10am'),('vishodhan','fe',1033,'esa','Male','asd','ddsa','dsa','TESLA','dsad','sad','b2','2019, 4, 13','10am'),('h','cas',1040,'csa','Male','ads','cas','cas','LANDROVER','cas','sad','c4','2019, 4, 18','10am'),('ritvik','dwq',1041,'dwq','Male','wdq','dwq','dwq','TESLA','dwq','wqd','a2','2019, 4, 18','10am'),('ritvij','ritvij iyer',1044,'THANE','Male','123747592','1234567890','MH-04-zz-1','TESLA','MODEL X','RED','b3','2019, 4, 19','10am'),('ritvij','wqd',1045,'dqwd','Male','wqd','dqwd','dwq','TESLA','dqwd','wqd','c2','2019, 4, 19','10am');
/*!40000 ALTER TABLE `bookingdetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-19 19:43:33
