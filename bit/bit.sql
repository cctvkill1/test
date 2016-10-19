/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50624
Source Host           : localhost:3306
Source Database       : bit

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2016-10-19 17:57:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for btc_cny
-- ----------------------------
DROP TABLE IF EXISTS `btc_cny`;
CREATE TABLE `btc_cny` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1888 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for btc_exchange_rate
-- ----------------------------
DROP TABLE IF EXISTS `btc_exchange_rate`;
CREATE TABLE `btc_exchange_rate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1514 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_future_index
-- ----------------------------
DROP TABLE IF EXISTS `btc_future_index`;
CREATE TABLE `btc_future_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1743 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_next_future_ticker
-- ----------------------------
DROP TABLE IF EXISTS `btc_next_future_ticker`;
CREATE TABLE `btc_next_future_ticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1321 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_quarter_future_ticker
-- ----------------------------
DROP TABLE IF EXISTS `btc_quarter_future_ticker`;
CREATE TABLE `btc_quarter_future_ticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1613 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_this_future_ticker
-- ----------------------------
DROP TABLE IF EXISTS `btc_this_future_ticker`;
CREATE TABLE `btc_this_future_ticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1617 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_usd
-- ----------------------------
DROP TABLE IF EXISTS `btc_usd`;
CREATE TABLE `btc_usd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1703 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for data
-- ----------------------------
DROP TABLE IF EXISTS `data`;
CREATE TABLE `data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `BTCCNY` float(11,4) DEFAULT NULL,
  `BTCExchange_rate` float(11,4) DEFAULT NULL,
  `BTCUSD` float(11,4) DEFAULT NULL,
  `BTCfuture_index` float(11,4) DEFAULT NULL,
  `BTCthis_future_ticker` float(11,4) DEFAULT NULL,
  `BTCnext_future_ticker` float(11,4) DEFAULT NULL,
  `BTCquarter_future_ticker` float(11,4) DEFAULT NULL,
  `LTCCNY` float(11,4) DEFAULT NULL,
  `LTCExchange_rate` float(11,4) DEFAULT NULL,
  `LTCUSD` float(11,4) DEFAULT NULL,
  `LTCFuture_index` float(11,4) DEFAULT NULL,
  `LTCthis_future_ticker` float(11,4) DEFAULT NULL,
  `LTCnext_future_ticker` float(11,4) DEFAULT NULL,
  `LTCquarter_future_ticker` float(11,4) DEFAULT NULL,
  `ct` float(20,4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=362 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for ltc_cny
-- ----------------------------
DROP TABLE IF EXISTS `ltc_cny`;
CREATE TABLE `ltc_cny` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1885 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for ltc_exchange_rate
-- ----------------------------
DROP TABLE IF EXISTS `ltc_exchange_rate`;
CREATE TABLE `ltc_exchange_rate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1056 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for ltc_future_index
-- ----------------------------
DROP TABLE IF EXISTS `ltc_future_index`;
CREATE TABLE `ltc_future_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1214 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for ltc_next_future_ticker
-- ----------------------------
DROP TABLE IF EXISTS `ltc_next_future_ticker`;
CREATE TABLE `ltc_next_future_ticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1530 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for ltc_quarter_future_ticker
-- ----------------------------
DROP TABLE IF EXISTS `ltc_quarter_future_ticker`;
CREATE TABLE `ltc_quarter_future_ticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1439 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for ltc_this_future_ticker
-- ----------------------------
DROP TABLE IF EXISTS `ltc_this_future_ticker`;
CREATE TABLE `ltc_this_future_ticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1726 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for ltc_usd
-- ----------------------------
DROP TABLE IF EXISTS `ltc_usd`;
CREATE TABLE `ltc_usd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1740 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
