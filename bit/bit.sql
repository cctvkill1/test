/*
Navicat MySQL Data Transfer

Source Server         : aliyun
Source Server Version : 50553
Source Host           : 123.56.9.210:3306
Source Database       : bit

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2016-12-06 17:49:05
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
  PRIMARY KEY (`id`),
  KEY `v` (`value`),
  KEY `c` (`ct`)
) ENGINE=InnoDB AUTO_INCREMENT=1894 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for btc_exchange_rate
-- ----------------------------
DROP TABLE IF EXISTS `btc_exchange_rate`;
CREATE TABLE `btc_exchange_rate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `v` (`value`),
  KEY `c` (`ct`)
) ENGINE=InnoDB AUTO_INCREMENT=1514 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_future_index
-- ----------------------------
DROP TABLE IF EXISTS `btc_future_index`;
CREATE TABLE `btc_future_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `v` (`value`),
  KEY `c` (`ct`)
) ENGINE=InnoDB AUTO_INCREMENT=1743 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_next_future_ticker
-- ----------------------------
DROP TABLE IF EXISTS `btc_next_future_ticker`;
CREATE TABLE `btc_next_future_ticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `v` (`value`),
  KEY `c` (`ct`)
) ENGINE=InnoDB AUTO_INCREMENT=1321 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_quarter_future_ticker
-- ----------------------------
DROP TABLE IF EXISTS `btc_quarter_future_ticker`;
CREATE TABLE `btc_quarter_future_ticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `v` (`value`),
  KEY `c` (`ct`)
) ENGINE=InnoDB AUTO_INCREMENT=1613 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_this_future_ticker
-- ----------------------------
DROP TABLE IF EXISTS `btc_this_future_ticker`;
CREATE TABLE `btc_this_future_ticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `v` (`value`),
  KEY `c` (`ct`)
) ENGINE=InnoDB AUTO_INCREMENT=1617 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for btc_trend
-- ----------------------------
DROP TABLE IF EXISTS `btc_trend`;
CREATE TABLE `btc_trend` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime DEFAULT NULL,
  `btc_future_index` float DEFAULT NULL,
  `btc_this_future_ticker` float DEFAULT NULL,
  `btc_next_future_ticker` float DEFAULT NULL,
  `btc_quarter_future_ticker` float DEFAULT NULL,
  `btc_cny` float DEFAULT NULL,
  `btc_exchange_rate` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `v` (`time`,`btc_future_index`,`btc_this_future_ticker`,`btc_next_future_ticker`,`btc_quarter_future_ticker`,`btc_cny`,`btc_exchange_rate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for btc_usd
-- ----------------------------
DROP TABLE IF EXISTS `btc_usd`;
CREATE TABLE `btc_usd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` float(14,4) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `v` (`value`),
  KEY `c` (`ct`)
) ENGINE=InnoDB AUTO_INCREMENT=1703 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
