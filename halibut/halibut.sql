-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: kettle
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `date` varchar(40) DEFAULT NULL,
  `timeconsuming` int DEFAULT NULL,
  `ip` varchar(40) DEFAULT NULL,
  `filesize` varchar(20) DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL,
  `transtype` varchar(2) DEFAULT NULL,
  `specialopt` varchar(2) DEFAULT NULL,
  `transmethod` varchar(2) DEFAULT NULL,
  `accesspattern` varchar(2) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `servicename` varchar(10) DEFAULT NULL,
  `authorize` varchar(2) DEFAULT NULL,
  `identified` varchar(2) DEFAULT NULL,
  `state` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES ('Sat Dec  3 21:42:34 2022',1,'113.57.80.53','85','/tuna.txt','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 30 17:16:46 2022',1,'113.57.80.53','437423','/textbook/refs/Maze.zip','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 30 17:16:19 2022',1,'113.57.80.53','51184','/textbook/refs/type.zip','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 30 09:10:22 2022',27,'113.57.80.53','54423256','/textbook/ppts/L9-步进式项目管理过程.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 30 09:10:06 2022',14,'113.57.80.53','19773351','/textbook/ppts/L8-集成系统管理概述.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 30 09:09:40 2022',1,'113.57.80.53','171370','/textbook/works/作业8-tuna.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 30 09:09:11 2022',1,'113.57.80.53','272','/buffalofish_score.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Sun Nov 27 14:17:13 2022',1,'113.57.80.53','73','/buffalofish.txt','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 23 10:24:13 2022',1,'113.57.80.64','159679','/textbook/works/作业7-buffalofish.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 23 10:24:02 2022',1,'113.57.80.64','40','/textbook/works/swordfish_answer.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Sep 26 22:51:39 2022',10,'113.57.80.52','27590088','/textbook/ppts/L0-关于本课程.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Sep 26 22:51:47 2022',6,'113.57.80.52','18469696','/textbook/ppts/L1-信息系统集成的概念.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Sep 26 22:52:08 2022',1,'113.57.80.52','134','/textbook/works/contact.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Sep 26 22:52:19 2022',1,'113.57.80.52','134','/textbook/works/contact.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Sep 26 23:02:11 2022',1,'113.57.80.52','107','/contact.txt','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Wed Sep 28 17:33:35 2022',1,'113.57.80.89','94289','/textbook/works/作业1-shark.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Sep 28 17:47:21 2022',9,'113.57.80.89','26497693','/textbook/refs/RESTful_Web_APIs中文版.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Sep 28 17:56:58 2022',5,'113.57.80.89','12514015','/textbook/ppts/L2-信息系统集成体系框架.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Sep 28 19:55:32 2022',1,'113.57.80.52','49','/shark.txt','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Mon Oct  3 15:53:03 2022',1,'113.57.80.43','37456','/textbook/announcement/ann1_作业提交注意事项.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Oct  3 15:53:09 2022',1,'113.57.80.43','37456','/textbook/announcement/ann1_作业提交注意事项.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Oct  5 09:59:36 2022',1,'113.57.80.86','266','/shark_score.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Oct 10 08:18:33 2022',23,'113.57.80.58','12633957','/textbook/ppts/L2-信息系统集成体系框架.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Oct 10 08:19:25 2022',71,'113.57.80.58','45161916','/textbook/ppts/L3-数据集成的框架.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Tue Oct 11 08:43:52 2022',1,'113.57.80.108','102351','/textbook/works/作业2-dolphin.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Thu Oct 13 21:15:11 2022',1,'113.57.80.29','49','/dolphin.txt','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Mon Oct 17 08:09:03 2022',39,'113.57.80.96','50835922','/textbook/ppts/L4-数据集成技术基础.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Fri Oct 21 14:05:36 2022',1,'113.57.80.76','268','/dolphin_score.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Oct 24 20:23:40 2022',1,'113.57.80.78','107196','/textbook/works/作业3-swordfish.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Oct 24 20:24:18 2022',24,'113.57.80.78','59646906','/textbook/ppts/L5---数据集成技术基础【续】.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Oct 26 21:42:17 2022',1,'113.57.80.42','51','/swordfish.txt','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov  2 08:05:40 2022',1,'113.57.80.18','342','/swordfish_score.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov  2 08:05:57 2022',1,'113.57.80.18','2328','/snapper.log','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov  2 08:06:43 2022',1,'113.57.80.18','98699','/textbook/works/综合作业-trout.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov  2 08:06:46 2022',1,'113.57.80.18','225328','/textbook/works/作业4-flounder.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov  2 08:15:02 2022',124,'113.57.80.18','36536197','/textbook/ppts/L6-服务集成概述.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Fri Nov  4 19:57:46 2022',1,'113.57.80.103','2328','/snapper.log','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Sat Nov  5 20:36:18 2022',1,'113.57.80.103','49','/flounder.txt','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov  9 08:25:06 2022',1,'113.57.80.82','269','/flounder_score.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov  9 08:25:37 2022',1,'113.57.80.82','90503','/textbook/works/作业5-octopus.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Sun Nov 13 18:06:24 2022',1,'113.57.80.125','49','/octopus.txt','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Sun Nov 13 18:07:24 2022',1,'113.57.80.125','91727','/time_dist.png','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Sun Nov 13 18:07:24 2022',1,'113.57.80.125','95502','/visit_per_day.png','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Sun Nov 13 18:07:24 2022',1,'113.57.80.125','353954','/index.html','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Sun Nov 13 18:07:24 2022',1,'113.57.80.125','150414','/overall.png','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Sun Nov 13 18:07:24 2022',1,'113.57.80.125','80276','/request.png','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 16 08:10:25 2022',1,'113.57.80.27','243','/trout_score.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 16 08:10:35 2022',1,'113.57.80.27','268','/octopus_score.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 16 08:11:16 2022',2,'113.57.80.27','123725','/textbook/works/作业6-salmon.pdf','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Wed Nov 16 08:14:05 2022',154,'113.57.80.27','31147206','/textbook/ppts/L7-RESTful服务集成.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','i'),('Wed Nov 16 08:38:14 2022',68,'113.57.80.27','75796617','/textbook/ppts/L7-RESTful服务集成.pptx','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Sun Nov 20 18:54:49 2022',1,'113.57.80.23','49','/salmon.txt','b','_','i','g','MaWenZhuo','ftp','0','*','c'),('Mon Nov 21 08:12:16 2022',1,'113.57.80.100','267','/salmon_score.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c'),('Mon Nov 21 08:51:08 2022',1,'113.57.80.100','243','/trout_score.txt','b','_','o','g','MaWenZhuo','ftp','0','*','c');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-07  2:42:51
