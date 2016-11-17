/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50624
Source Host           : localhost:3306
Source Database       : xx007

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2016-11-17 14:51:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `weixin` varchar(255) DEFAULT NULL,
  `alipay` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `nong_hang` varchar(255) DEFAULT NULL,
  `zhong_hang` varchar(255) DEFAULT NULL,
  `jian_hang` varchar(255) DEFAULT NULL,
  `gong_hang` varchar(255) DEFAULT NULL,
  `you_zheng` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `qq` varchar(255) DEFAULT NULL,
  `lv` varchar(255) DEFAULT NULL,
  `credit_point` varchar(255) DEFAULT NULL,
  `score_number` int(11) DEFAULT NULL,
  `post_number` int(11) DEFAULT NULL,
  `post_point` varchar(255) DEFAULT NULL,
  `register_time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
