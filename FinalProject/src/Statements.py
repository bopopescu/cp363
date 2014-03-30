'''
Created on 2014-03-25

@author: mo
'''
TABLES = {}
TABLES['Employee'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`Employee` ("
    "`eid` INT NOT NULL AUTO_INCREMENT,"
    "`ename` VARCHAR(45) NULL,"
    "`salary` DECIMAL NULL,"
    "`date_of_employment` VARCHAR(45) NULL,"
    "`date_of_departure` VARCHAR(45) NULL,"
    "`is_manager` TINYINT(1) NULL,"
    "`manager_id` INT NULL,"
    "PRIMARY KEY (`eid`))"
    "ENGINE = InnoDB")
TABLES['Expenses'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`Expenses` ("
    "`xid` INT NOT NULL AUTO_INCREMENT,"
    "`date` VARCHAR(45) NULL,"
    "`cost` DECIMAL NULL,"
    "`details` VARCHAR(400) NULL,"
    "PRIMARY KEY (`xid`))"
    "ENGINE = InnoDB")
TABLES['UpdateExpenses'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`UpdateExpenses` ("
    "`ueid` INT NOT NULL AUTO_INCREMENT,"
    "`eid` INT NOT NULL,"
    "`xid` INT NOT NULL,"
    "PRIMARY KEY (`ueid`, `eid`, `xid`),"
    "INDEX `eid_idx` (`eid` ASC),"
    "INDEX `xid_idx` (`xid` ASC),"
    "CONSTRAINT `eid`"
    "    FOREIGN KEY (`eid`)"
    "    REFERENCES `CarCompany`.`Employee` (`eid`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION,"
    "CONSTRAINT `xid`"
    "    FOREIGN KEY (`xid`)"
    "    REFERENCES `CarCompany`.`Expenses` (`xid`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION)"
    "ENGINE = InnoDB")
TABLES['Cars'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`Cars` ("
    "`vin` VARCHAR(20) NOT NULL,"
    "`make` VARCHAR(45) NULL,"
    "`model` VARCHAR(45) NULL,"
    "`colour` VARCHAR(45) NULL,"
    "`year` INT NULL,"
    "`sold` TINYINT(1) NULL,"
    "`price` DECIMAL NULL,"
    "PRIMARY KEY (`vin`))"
    "ENGINE = InnoDB")
TABLES['UpdateCars'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`UpdateCars` ("
    "`ucid` INT NOT NULL AUTO_INCREMENT,"
    "`eid` INT NOT NULL,"
    "`vin` VARCHAR(20) NOT NULL,"
    "`date` VARCHAR(45) NULL,"
    "`change` VARCHAR(400) NULL,"
    "PRIMARY KEY (`ucid`, `eid`, `vin`),"
    "INDEX `vin_idx` (`vin` ASC),"
    "INDEX `eid_idx` (`eid` ASC),"
    "CONSTRAINT `eid2`"
    "    FOREIGN KEY (`eid`)"
    "    REFERENCES `CarCompany`.`Employee` (`eid`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION,"
    "CONSTRAINT `vin2`"
    "    FOREIGN KEY (`vin`)"
    "    REFERENCES `CarCompany`.`Cars` (`vin`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION)"
    "ENGINE = InnoDB")
TABLES['Suppliers'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`Suppliers` ("
    "`sid` INT NOT NULL AUTO_INCREMENT,"
    "`sname` VARCHAR(45) NULL,"
    "`phone` VARCHAR(45) NULL,"
    "`postal_code` VARCHAR(45) NULL,"
    "`street` VARCHAR(45) NULL,"
    "`city` VARCHAR(45) NULL,"
    "`country` VARCHAR(45) NULL,"
    "`province` VARCHAR(45) NULL,"
    "PRIMARY KEY (`sid`))"
    "ENGINE = InnoDB")
TABLES['CarSupply'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`CarSupply` ("
    "`sid` INT NOT NULL,"
    "`vin` VARCHAR(20) NOT NULL,"
    "`date_supplied` VARCHAR(45) NULL,"
    "PRIMARY KEY (`sid`, `vin`),"
    "INDEX `sid_idx` (`sid` ASC),"
    "INDEX `vin_idx` (`vin` ASC),"
    "CONSTRAINT `sid3`"
    "    FOREIGN KEY (`sid`)"
    "    REFERENCES `CarCompany`.`Suppliers` (`sid`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION,"
    "CONSTRAINT `vin3`"
    "    FOREIGN KEY (`vin`)"
    "    REFERENCES `CarCompany`.`Cars` (`vin`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION)"
    "ENGINE = InnoDB")
TABLES['WorksWith'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`WorksWith` ("
    "`eid` INT NOT NULL,"
    "`sid` INT NOT NULL,"
    "`date` VARCHAR(45) NULL,"
    "PRIMARY KEY (`eid`, `sid`),"
    "INDEX `eid_idx` (`eid` ASC),"
    "INDEX `sid_idx` (`sid` ASC),"
    "CONSTRAINT `eid4`"
    "    FOREIGN KEY (`eid`)"
    "    REFERENCES `CarCompany`.`Employee` (`eid`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION,"
    "CONSTRAINT `sid4`"
    "    FOREIGN KEY (`sid`)"
    "    REFERENCES `CarCompany`.`Suppliers` (`sid`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION)"
    "ENGINE = InnoDB")
TABLES['Customer'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`Customer` ("
    "`cid` INT NOT NULL AUTO_INCREMENT,"
    "`cname` VARCHAR(45) NULL,"
    "`join_date` VARCHAR(45) NULL,"
    "`phone` VARCHAR(45) NULL,"
    "PRIMARY KEY (`cid`))"
    "ENGINE = InnoDB")
TABLES['HasCustomer'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`HasCustomer` ("
    "`eid` INT NOT NULL,"
    "`cid` INT NOT NULL,"
    "`date` VARCHAR(45) NULL,"
    "`details` VARCHAR(400) NULL,"
    "PRIMARY KEY (`eid`, `cid`),"
    "INDEX `eid_idx` (`eid` ASC),"
    "INDEX `cid_idx` (`cid` ASC),"
    "CONSTRAINT `eid5`"
    "    FOREIGN KEY (`eid`)"
    "    REFERENCES `CarCompany`.`Employee` (`eid`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION,"
    "CONSTRAINT `cid5`"
    "    FOREIGN KEY (`cid`)"
    "    REFERENCES `CarCompany`.`Customer` (`cid`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION)"
    "ENGINE = InnoDB")
TABLES['CustomerPurchases'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`CustomerPurchases` ("
    "`cid` INT NOT NULL,"
    "`vin` VARCHAR(20) NOT NULL,"
    "PRIMARY KEY (`cid`, `vin`),"
    "INDEX `cid_idx` (`cid` ASC),"
    "INDEX `vin_idx` (`vin` ASC),"
    "CONSTRAINT `cid6`"
    "    FOREIGN KEY (`cid`)"
    "    REFERENCES `CarCompany`.`Customer` (`cid`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION,"
    "CONSTRAINT `vin6`"
    "    FOREIGN KEY (`vin`)"
    "    REFERENCES `CarCompany`.`Cars` (`vin`)"
    "    ON DELETE NO ACTION"
    "    ON UPDATE NO ACTION)"
    "ENGINE = InnoDB")
TABLES['Logins'] = (
    "CREATE TABLE IF NOT EXISTS `CarCompany`.`Logins` ("
    "`eid` INT NOT NULL UNIQUE,"
    "`username` VARCHAR(8) NOT NULL UNIQUE,"
    "`password` VARCHAR(8) NOT NULL,"
    "PRIMARY KEY (`eid`),"
    "CONSTRAINT `eid6`"
    "    FOREIGN KEY (`eid`)"
    "    REFERENCES `CarCompany`.`Employee` (`eid`)"
    "    ON DELETE CASCADE"
    "    ON UPDATE NO ACTION)")

INSERT = {}
INSERT['Employee'] = (
    "INSERT INTO `CarCompany`.`Employee`"
    "    (`ename`, `salary`, `date_of_employment`, `date_of_departure`, `is_manager`, `manager_id`)"
    "    VALUES (%s, %s, %s, %s, %s, %s)")
INSERT['Login'] = (
    "INSERT INTO `CarCompany`.`Logins`"
    "    (`eid`, `username`, `password`)"
    "    VALUES (%s, %s, %s)")
INSERT['Expenses'] = (
    "INSERT INTO `CarCompany`.`Expenses` (`date`, `cost`, `details`)"
    "    VALUES (%s, %s, %s)")
INSERT['UpdateExpenses'] = (
    "INSERT INTO `CarCompany`.`UpdateExpenses` (`eid`, `xid`)"
    "    VALUES (%s, %s)")
INSERT['Cars'] = (
    "INSERT INTO `CarCompany`.`Cars`"
    "    (`vin`, `make`, `model`, `year`, `colour`, `sold`, `price`)"
    "    VALUES (%s, %s, %s, %s, %s, %s, %s)")
INSERT['UpdateCars'] = (
    "INSERT INTO `CarCompany`.`UpdateCars` (`eid`, `vin`, `date`, `change`)"
    "    VALUES (%s, %s, %s, %s)")
INSERT['Suppliers'] = (
    "INSERT INTO `CarCompany`.`Suppliers` (`sname`, `phone`, `postal_code`, `street`, `city`, `country`, `province`)"
    "    VALUES (%s, %s, %s, %s, %s, %s, %s)")
INSERT['CarSupply'] = (
    "INSERT INTO `CarCompany`.`CarSupply` (`sid`, `vin`, `date_supplied`)"
    "    VALUES (%s, %s, %s)")
INSERT['WorksWith'] = (
    "INSERT INTO `CarCompany`.`WorksWith` (`eid`, `sid`, `date`)"
    "    VALUES (%s, %s, %s)")
INSERT['Customer'] = (
    "INSERT INTO `CarCompany`.`Customer` (`cname`, `join_date`, `phone`)"
    "    VALUES (%s, %s, %s)")
INSERT['HasCustomer'] = (
    "INSERT INTO `CarCompany`.`HasCustomer` (`eid`, `cid`, `date`, `details`)"
    "    VALUES (%s, %s, %s, %s)")
INSERT['CustomerPurchases'] = (
    "INSERT INTO `CarCompany`.`CustomerPurchases` (`cid`, `vin`)"
    "    VALUES (%s, %s)")
USER_LOGIN = (
    "SELECT * FROM `CarCompany`.`Employee` WHERE `eid`=("
    "    SELECT `eid` FROM `CarCompany`.`Logins` WHERE `username`=%s AND `password`=%s LIMIT 1"
    ")")