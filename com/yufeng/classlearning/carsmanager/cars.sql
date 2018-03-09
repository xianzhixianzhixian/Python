CREATE TABLE `cars` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '数据的主键',
  `carnum` varchar(50) NOT NULL DEFAULT '' COMMENT '车牌号',
  `carname` varchar(20) NOT NULL DEFAULT '' COMMENT '车名',
  `carcolor` varchar(20) NOT NULL DEFAULT '' COMMENT '车的颜色',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '在库状态，0表示空闲，1表示繁忙，默认为0',
  `daypay` double NOT NULL DEFAULT '0' COMMENT '日租金',
  `is_delete` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否报废，0表示否，1表示是，默认为0',
  `create_time` timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) COMMENT '创建记录的时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新的时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
