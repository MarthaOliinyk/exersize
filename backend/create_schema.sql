-- MySQL Script generated by MySQL Workbench
-- Fri Sep 23 15:28:26 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema exersize
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `exersize`;

-- -----------------------------------------------------
-- Schema exersize
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `exersize` DEFAULT CHARACTER SET utf8;
USE `exersize`;

-- -----------------------------------------------------
-- Table `exersize`.`role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `exersize`.`role`;

CREATE TABLE IF NOT EXISTS `exersize`.`role` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exersize`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `exersize`.`user`;

CREATE TABLE IF NOT EXISTS `exersize`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `registration_date` DATE NOT NULL,
  `role_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_user_role`
    FOREIGN KEY (`role_id`)
    REFERENCES `exersize`.`role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `email_UNIQUE` ON `exersize`.`user` (`email` ASC);

CREATE INDEX `fk_user_role_idx` ON `exersize`.`user` (`role_id` ASC);


-- -----------------------------------------------------
-- Table `exersize`.`course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `exersize`.`course`;

CREATE TABLE IF NOT EXISTS `exersize`.`course` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exersize`.`subscription_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `exersize`.`subscription_type`;

CREATE TABLE IF NOT EXISTS `exersize`.`subscription_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `session_count` INT NOT NULL,
  `duration` INT NOT NULL,
  `price` DECIMAL(10,2) NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_subscription_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `exersize`.`course` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_subscription_course1_idx` ON `exersize`.`subscription_type` (`course_id` ASC);


-- -----------------------------------------------------
-- Table `exersize`.`user_has_course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `exersize`.`user_has_course`;

CREATE TABLE IF NOT EXISTS `exersize`.`user_has_course` (
  `user_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `course_id`),
  CONSTRAINT `fk_user_has_course_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `exersize`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_course_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `exersize`.`course` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_user_has_course_course1_idx` ON `exersize`.`user_has_course` (`course_id` ASC);

CREATE INDEX `fk_user_has_course_user1_idx` ON `exersize`.`user_has_course` (`user_id` ASC);


-- -----------------------------------------------------
-- Table `exersize`.`schedule`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `exersize`.`schedule`;

CREATE TABLE IF NOT EXISTS `exersize`.`schedule` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `start` DATETIME NOT NULL,
  `end` DATETIME NOT NULL,
  `participants` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_schedule_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `exersize`.`course` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_schedule_course1_idx` ON `exersize`.`schedule` (`course_id` ASC);


-- -----------------------------------------------------
-- Table `exersize`.`appointment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `exersize`.`appointment`;

CREATE TABLE IF NOT EXISTS `exersize`.`appointment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `time` DATETIME NOT NULL,
  `schedule_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_appointment_schedule1`
    FOREIGN KEY (`schedule_id`)
    REFERENCES `exersize`.`schedule` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_appointment_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `exersize`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_appointment_schedule1_idx` ON `exersize`.`appointment` (`schedule_id` ASC);

CREATE INDEX `fk_appointment_user1_idx` ON `exersize`.`appointment` (`user_id` ASC);


-- -----------------------------------------------------
-- Table `exersize`.`subscription`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `exersize`.`subscription`;

CREATE TABLE IF NOT EXISTS `exersize`.`subscription` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `start` DATETIME NOT NULL,
  `end` DATETIME NOT NULL,
  `user_id` INT NOT NULL,
  `subscription_type_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_subscription_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `exersize`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_subscription_subscription_type1`
    FOREIGN KEY (`subscription_type_id`)
    REFERENCES `exersize`.`subscription_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_subscription_user1_idx` ON `exersize`.`subscription` (`user_id` ASC);

CREATE INDEX `fk_subscription_subscription_type1_idx` ON `exersize`.`subscription` (`subscription_type_id` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;