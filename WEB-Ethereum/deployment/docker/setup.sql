CREATE DATABASE /*!32312 IF NOT EXISTS*/ `haozi` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `haozi`;

--
-- Table structure for table `secrets`
--

DROP TABLE IF EXISTS `secrets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `secrets` (
  `session_id` varchar(50) DEFAULT NULL,
  `secret` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `secrets`
--

LOCK TABLES `secrets` WRITE;
/*!40000 ALTER TABLE `secrets` DISABLE KEYS */;
INSERT INTO `secrets` VALUES ('secret key in ropsten network','386BD35D089B7D6FDB7DDF0FDA67E3F0801DB92BC215909D89A92876E5F13250');
/*!40000 ALTER TABLE `secrets` ENABLE KEYS */;
UNLOCK TABLES;
