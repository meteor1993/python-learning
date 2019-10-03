SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for spider_data
-- ----------------------------
DROP TABLE IF EXISTS `spider_data`;
CREATE TABLE `spider_data`  (
  `id` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '主键 UUID',
  `plantform` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '平台类型',
  `read_num` int(11) NULL DEFAULT NULL COMMENT '总阅读数',
  `fans_num` int(11) NULL DEFAULT NULL COMMENT '总粉丝数',
  `rank_num` int(11) NULL DEFAULT NULL COMMENT '排名',
  `like_num` int(11) NULL DEFAULT NULL COMMENT '总点赞数',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
