# Host: 
# Database: test
# Table: 'category'
# 
CREATE TABLE `category` (
  `uid` BIGINT UNSIGNED NOT NULL,
  `category_uid` BIGINT UNSIGNED default '0',
  `base_category_uid` BIGINT UNSIGNED default '0',
  `category_strict_membership` tinyint(1) default '0',
  KEY `uid` (`uid`),
  KEY `category_strict_membership` (`category_strict_membership`),
  KEY `Membership` (`category_uid`,`base_category_uid`),
  KEY `FuzzyMembership` (`category_uid`)
) TYPE = ndb; 
