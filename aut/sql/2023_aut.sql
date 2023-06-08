# Honvédelmi adatok 2023-ra az autentikusból
# Készítette: Konta Boáz (kontab6@gmail.com).
USE honved2;
SET GLOBAL max_allowed_packet=524288000;
DELETE FROM aut WHERE datum >= '2023-01-01';
INSERT INTO aut (sorsz,datum,ceg,kezd,hely,musor,kontakt,megjegyzes,helykod,szallitas,tev) VALUES 
