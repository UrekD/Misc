-- --------------------------------------------------------
-- Host:                         172.22.2.22
-- Server version:               8.0.31 - MySQL Community Server - GPL
-- Server OS:                    Linux
-- HeidiSQL Version:             12.1.0.6557
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for aboutyou
DROP DATABASE IF EXISTS `aboutyou`;
CREATE DATABASE IF NOT EXISTS `aboutyou` /*!40100 DEFAULT CHARACTER SET utf32 COLLATE utf32_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `aboutyou`;

-- Dumping structure for table aboutyou.main
DROP TABLE IF EXISTS `main`;
CREATE TABLE IF NOT EXISTS `main` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `URL` varchar(999) CHARACTER SET armscii8 COLLATE armscii8_bin NOT NULL DEFAULT '',
  `PRICE` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Dumping data for table aboutyou.main: ~2 rows (approximately)
DELETE FROM `main`;
INSERT INTO `main` (`ID`, `URL`, `PRICE`) VALUES
	(1, 'https://www.aboutyou.si/p/adidas-sportswear/sportna-trenirka-6903217?vid=46432862', 999),
	(2, 'https://www.aboutyou.si/p/selected-homme/suknjic-josh-8363888?vid=51358306', 999);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
