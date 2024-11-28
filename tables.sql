USE investments;
DROP TABLE IF EXISTS caucion;
 
 CREATE TABLE `caucion` (
  `caucion_id` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL,
  `monto` FLOAT NOT NULL,
  `tna` FLOAT NOT NULL,
  `comision` FLOAT NOT NULL,
  `dias` INT NOT NULL,
  `derecho_mercado` FLOAT NOT NULL,
  PRIMARY KEY (`caucion_id`)
) ENGINE=InnoDB;