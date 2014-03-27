SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `CarCompany` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `CarCompany` ;

-- -----------------------------------------------------
-- Table `CarCompany`.`Employee`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`Employee` (
  `eid` INT NOT NULL ,
  `ename` VARCHAR(45) NULL ,
  `salary` DECIMAL NULL ,
  `date_of_employment` VARCHAR(45) NULL ,
  `date_of_departure` VARCHAR(45) NULL ,
  `is_manager` TINYINT(1) NULL ,
  `manager_id` INT NULL ,
  PRIMARY KEY (`eid`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`Expenses`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`Expenses` (
  `xid` INT NOT NULL ,
  `date` VARCHAR(45) NULL ,
  `cost` DECIMAL NULL ,
  `details` VARCHAR(400) NULL ,
  PRIMARY KEY (`xid`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`UpdateExpenses`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`UpdateExpenses` (
  `eid` INT NOT NULL ,
  `xid` INT NOT NULL ,
  PRIMARY KEY (`eid`, `xid`) ,
  INDEX `eid_idx` (`eid` ASC) ,
  INDEX `xid_idx` (`xid` ASC) ,
  CONSTRAINT `eid`
    FOREIGN KEY (`eid` )
    REFERENCES `CarCompany`.`Employee` (`eid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `xid`
    FOREIGN KEY (`xid` )
    REFERENCES `CarCompany`.`Expenses` (`xid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`Cars`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`Cars` (
  `vin` INT NOT NULL ,
  `make` VARCHAR(45) NULL ,
  `model` VARCHAR(45) NULL ,
  `colour` VARCHAR(45) NULL ,
  `year` INT NULL ,
  `sold` TINYINT(1) NULL ,
  `price` DECIMAL NULL ,
  PRIMARY KEY (`vin`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`UpdateCars`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`UpdateCars` (
  `eid` INT NOT NULL ,
  `vin` INT NOT NULL ,
  `date` VARCHAR(45) NULL ,
  `change` VARCHAR(400) NULL ,
  PRIMARY KEY (`eid`, `vin`) ,
  INDEX `vin_idx` (`vin` ASC) ,
  INDEX `eid_idx` (`eid` ASC) ,
  CONSTRAINT `eid`
    FOREIGN KEY (`eid` )
    REFERENCES `CarCompany`.`Employee` (`eid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `vin`
    FOREIGN KEY (`vin` )
    REFERENCES `CarCompany`.`Cars` (`vin` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`Suppliers`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`Suppliers` (
  `sid` INT NOT NULL ,
  `sname` VARCHAR(45) NULL ,
  `phone` VARCHAR(45) NULL ,
  `postal_code` VARCHAR(45) NULL ,
  `street` VARCHAR(45) NULL ,
  `city` VARCHAR(45) NULL ,
  `country` VARCHAR(45) NULL ,
  `province` VARCHAR(45) NULL ,
  PRIMARY KEY (`sid`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`CarSupply`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`CarSupply` (
  `sid` INT NOT NULL ,
  `vin` INT NOT NULL ,
  `date_supplied` VARCHAR(45) NULL ,
  PRIMARY KEY (`sid`, `vin`) ,
  INDEX `sid_idx` (`sid` ASC) ,
  INDEX `vin_idx` (`vin` ASC) ,
  CONSTRAINT `sid`
    FOREIGN KEY (`sid` )
    REFERENCES `CarCompany`.`Suppliers` (`sid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `vin`
    FOREIGN KEY (`vin` )
    REFERENCES `CarCompany`.`Cars` (`vin` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`WorksWith`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`WorksWith` (
  `eid` INT NOT NULL ,
  `sid` INT NOT NULL ,
  `date` VARCHAR(45) NULL ,
  PRIMARY KEY (`eid`, `sid`) ,
  INDEX `eid_idx` (`eid` ASC) ,
  INDEX `sid_idx` (`sid` ASC) ,
  CONSTRAINT `eid`
    FOREIGN KEY (`eid` )
    REFERENCES `CarCompany`.`Employee` (`eid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `sid`
    FOREIGN KEY (`sid` )
    REFERENCES `CarCompany`.`Suppliers` (`sid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`Customer`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`Customer` (
  `cid` INT NOT NULL ,
  `cname` VARCHAR(45) NULL ,
  `join_date` VARCHAR(45) NULL ,
  `phone` VARCHAR(45) NULL ,
  PRIMARY KEY (`cid`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`HasCustomer`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`HasCustomer` (
  `eid` INT NOT NULL ,
  `cid` INT NOT NULL ,
  `date` VARCHAR(45) NULL ,
  `details` VARCHAR(400) NULL ,
  PRIMARY KEY (`eid`, `cid`) ,
  INDEX `eid_idx` (`eid` ASC) ,
  INDEX `cid_idx` (`cid` ASC) ,
  CONSTRAINT `eid`
    FOREIGN KEY (`eid` )
    REFERENCES `CarCompany`.`Employee` (`eid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `cid`
    FOREIGN KEY (`cid` )
    REFERENCES `CarCompany`.`Customer` (`cid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CarCompany`.`CustomerPurchases`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `CarCompany`.`CustomerPurchases` (
  `cid` INT NOT NULL ,
  `vin` INT NOT NULL ,
  PRIMARY KEY (`cid`, `vin`) ,
  INDEX `cid_idx` (`cid` ASC) ,
  INDEX `vin_idx` (`vin` ASC) ,
  CONSTRAINT `cid`
    FOREIGN KEY (`cid` )
    REFERENCES `CarCompany`.`Customer` (`cid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `vin`
    FOREIGN KEY (`vin` )
    REFERENCES `CarCompany`.`Cars` (`vin` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `CarCompany` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`Employee`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`Employee` (`eid`, `ename`, `salary`, `date_of_employment`, `date_of_departure`, `is_manager`, `manager_id`) VALUES (1, 'bryan', 5000, 'March 1, 2014', NULL, 1, 1);
INSERT INTO `CarCompany`.`Employee` (`eid`, `ename`, `salary`, `date_of_employment`, `date_of_departure`, `is_manager`, `manager_id`) VALUES (2, 'mohamed', 4000, 'March 2, 2014', NULL, 0, 1);

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`Expenses`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`Expenses` (`xid`, `date`, `cost`, `details`) VALUES (1, 'March 1, 2014', 5000, 'create company');
INSERT INTO `CarCompany`.`Expenses` (`xid`, `date`, `cost`, `details`) VALUES (2, 'March 1, 2014', 30000, 'buy cars');

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`UpdateExpenses`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`UpdateExpenses` (`eid`, `xid`) VALUES (1, 1);
INSERT INTO `CarCompany`.`UpdateExpenses` (`eid`, `xid`) VALUES (1, 2);

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`Cars`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`Cars` (`vin`, `make`, `model`, `colour`, `year`, `sold`, `price`) VALUES (666, 'Toyota', 'somemodel', 'red', 2014, 0, 32000);
INSERT INTO `CarCompany`.`Cars` (`vin`, `make`, `model`, `colour`, `year`, `sold`, `price`) VALUES (667, 'Toyota', 'somemodel', 'red', 2014, 0, 32000);

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`UpdateCars`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`UpdateCars` (`eid`, `vin`, `date`, `change`) VALUES (1, 666, 'March 10, 2014', 'update car price change');

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`Suppliers`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`Suppliers` (`sid`, `sname`, `phone`, `postal_code`, `street`, `city`, `country`, `province`) VALUES (1, 'Toyota', '1112223333', 'M2M2M2', 'fakestreet avenue', 'Toronto', 'Canada', 'Ontario');

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`CarSupply`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`CarSupply` (`sid`, `vin`, `date_supplied`) VALUES (1, 666, 'March 10, 2014');

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`WorksWith`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`WorksWith` (`eid`, `sid`, `date`) VALUES (1, 1, 'March 10, 2014');

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`Customer`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`Customer` (`cid`, `cname`, `join_date`, `phone`) VALUES (1, 'bob', 'March 10, 2014', '1112223333');
INSERT INTO `CarCompany`.`Customer` (`cid`, `cname`, `join_date`, `phone`) VALUES (2, 'mary', 'March 10, 2014', '1112223333');

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`HasCustomer`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`HasCustomer` (`eid`, `cid`, `date`, `details`) VALUES (1, 1, 'March 10, 2014', 'sold car');
INSERT INTO `CarCompany`.`HasCustomer` (`eid`, `cid`, `date`, `details`) VALUES (1, 2, 'March 10, 2013', 'sold car');

COMMIT;

-- -----------------------------------------------------
-- Data for table `CarCompany`.`CustomerPurchases`
-- -----------------------------------------------------
START TRANSACTION;
USE `CarCompany`;
INSERT INTO `CarCompany`.`CustomerPurchases` (`cid`, `vin`) VALUES (1, 666);
INSERT INTO `CarCompany`.`CustomerPurchases` (`cid`, `vin`) VALUES (2, 667);

COMMIT;
