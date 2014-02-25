-- ----------------------------------------------------
-- Bryan Chau & Mohamed Mohamedtaki
-- CP363 Assignment 3
-- ----------------------------------------------------
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `a3` DEFAULT CHARACTER SET utf8 ;
USE `a3` ;

-- -----------------------------------------------------
-- Table `a3`.`Parts`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `a3`.`Parts` (
  `pid` VARCHAR(10) NOT NULL ,
  `pname` VARCHAR(100) NOT NULL ,
  `colour` VARCHAR(100) NOT NULL ,
  PRIMARY KEY (`pid`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `a3`.`Suppliers`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `a3`.`Suppliers` (
  `sid` VARCHAR(10) NOT NULL ,
  `sname` VARCHAR(100) NOT NULL ,
  `address` VARCHAR(100) NOT NULL ,
  PRIMARY KEY (`sid`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `a3`.`Catalog`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `a3`.`Catalog` (
  `sid` VARCHAR(10) NOT NULL ,
  `pid` VARCHAR(10) NOT NULL ,
  `cost` INT NOT NULL ,
  PRIMARY KEY (`sid`, `pid`) ,
  INDEX `pid_idx` (`pid` ASC) ,
  INDEX `sid_idx` (`sid` ASC) ,
  CONSTRAINT `pid`
    FOREIGN KEY (`pid` )
    REFERENCES `a3`.`Parts` (`pid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `sid`
    FOREIGN KEY (`sid` )
    REFERENCES `a3`.`Suppliers` (`sid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `a3` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `a3`.`Parts`
-- -----------------------------------------------------
START TRANSACTION;
USE `a3`;
INSERT INTO `a3`.`Parts` (`pid`, `pname`, `colour`) VALUES ('p1', 'nut', 'red');
INSERT INTO `a3`.`Parts` (`pid`, `pname`, `colour`) VALUES ('p2', 'bolt', 'green');
INSERT INTO `a3`.`Parts` (`pid`, `pname`, `colour`) VALUES ('p3', 'screw', 'red');
INSERT INTO `a3`.`Parts` (`pid`, `pname`, `colour`) VALUES ('p4', 'cam', 'blue');
INSERT INTO `a3`.`Parts` (`pid`, `pname`, `colour`) VALUES ('p5', 'cog', 'green');
INSERT INTO `a3`.`Parts` (`pid`, `pname`, `colour`) VALUES ('p6', 'nail', 'green');

COMMIT;

-- -----------------------------------------------------
-- Data for table `a3`.`Suppliers`
-- -----------------------------------------------------
START TRANSACTION;
USE `a3`;
INSERT INTO `a3`.`Suppliers` (`sid`, `sname`, `address`) VALUES ('s1', 'smith', 'london');
INSERT INTO `a3`.`Suppliers` (`sid`, `sname`, `address`) VALUES ('s2', 'jones', 'paris');
INSERT INTO `a3`.`Suppliers` (`sid`, `sname`, `address`) VALUES ('s3', 'blake', 'paris');
INSERT INTO `a3`.`Suppliers` (`sid`, `sname`, `address`) VALUES ('s4', 'clark', 'london');
INSERT INTO `a3`.`Suppliers` (`sid`, `sname`, `address`) VALUES ('s5', 'adams', 'toronto');
INSERT INTO `a3`.`Suppliers` (`sid`, `sname`, `address`) VALUES ('s6', 'peter', 'waterloo');

COMMIT;

-- -----------------------------------------------------
-- Data for table `a3`.`Catalog`
-- -----------------------------------------------------
START TRANSACTION;
USE `a3`;
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s1', 'p1', 200);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s1', 'p4', 300);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s2', 'p1', 100);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s2', 'p2', 400);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s2', 'p3', 200);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s2', 'p4', 300);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s2', 'p5', 100);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s2', 'p6', 800);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s3', 'p2', 200);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s3', 'p5', 400);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s4', 'p4', 400);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s5', 'p1', 100);
INSERT INTO `a3`.`Catalog` (`sid`, `pid`, `cost`) VALUES ('s5', 'p2', 200);

COMMIT;