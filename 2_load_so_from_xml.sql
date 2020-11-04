USE `sotorrent18_09`;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE '/mnt/e/data_dump_final_path/Users.xml'
INTO TABLE `Users`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE '/mnt/e/data_dump_final_path/Badges.xml'
INTO TABLE `Badges`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE '/mnt/e/data_dump_final_path/Posts.xml'
INTO TABLE `Posts`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE '/mnt/e/data_dump_final_path/Comments.xml'
INTO TABLE `Comments`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE '/mnt/e/data_dump_final_path/PostHistory.xml'
INTO TABLE `PostHistory`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE '/mnt/e/data_dump_final_path/PostLinks.xml'
INTO TABLE `PostLinks`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE '/mnt/e/data_dump_final_path/Tags.xml'
INTO TABLE `Tags`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE '/mnt/e/data_dump_final_path/Votes.xml'
INTO TABLE `Votes`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;
