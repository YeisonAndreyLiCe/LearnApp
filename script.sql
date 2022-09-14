-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema learn_app
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `learn_app` ;

-- -----------------------------------------------------
-- Schema learn_app
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `learn_app` DEFAULT CHARACTER SET utf8 ;
USE `learn_app` ;

-- -----------------------------------------------------
-- Table `learn_app`.`roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `learn_app`.`roles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `rol` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `learn_app`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `learn_app`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `birth_date` DATE NOT NULL,
  `email` VARCHAR(150) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `rol_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_roles1_idx` (`rol_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_roles1`
    FOREIGN KEY (`rol_id`)
    REFERENCES `learn_app`.`roles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `learn_app`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `learn_app`.`categories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(80) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `learn_app`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `learn_app`.`courses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL,
  `description` TEXT(10000) NULL,
  `instructor_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_courses_users1_idx` (`instructor_id` ASC) VISIBLE,
  INDEX `fk_courses_categories1_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_courses_users1`
    FOREIGN KEY (`instructor_id`)
    REFERENCES `learn_app`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_courses_categories1`
    FOREIGN KEY (`category_id`)
    REFERENCES `learn_app`.`categories` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `learn_app`.`records`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `learn_app`.`records` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `course_id` INT NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `record` BLOB NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_records_courses1_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `fk_records_courses1`
    FOREIGN KEY (`course_id`)
    REFERENCES `learn_app`.`courses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `learn_app`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `learn_app`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `comment` VARCHAR(200) NULL,
  `rate` TINYINT(1) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_comments_courses1_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `learn_app`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_courses1`
    FOREIGN KEY (`course_id`)
    REFERENCES `learn_app`.`courses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `learn_app`.`users_has_courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `learn_app`.`users_has_courses` (
  `user_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`, `course_id`),
  INDEX `fk_users_has_courses_courses1_idx` (`course_id` ASC) VISIBLE,
  INDEX `fk_users_has_courses_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_courses_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `learn_app`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_courses_courses1`
    FOREIGN KEY (`course_id`)
    REFERENCES `learn_app`.`courses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

ALTER TABLE `learn_app`.`records`
CHANGE COLUMN `record` `record` VARCHAR(250) NOT NULL ;

INSERT INTO `learn_app`.`roles` (`id`, `rol`) VALUES ('1', 'Admin');
INSERT INTO `learn_app`.`roles` (`id`, `rol`) VALUES ('2', 'Instructor');
INSERT INTO `learn_app`.`roles` (`id`, `rol`) VALUES ('3', 'Student');
INSERT INTO `learn_app`.`categories` (`id`, `name`, `description`) VALUES ('2', 'UX', 'Cursos de experiencia de usuario');
INSERT INTO `learn_app`.`courses` (`name`, `description`, `instructor_id`, `category_id`) VALUES ('U/X desing responsive', 'A course about desin gresponsive', '1', '2');




SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
