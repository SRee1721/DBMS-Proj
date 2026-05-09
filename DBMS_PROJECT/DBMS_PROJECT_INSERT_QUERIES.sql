INSERT INTO TRAIN 
VALUES(
    'T100','VAIGAI','EXPRESS'
);
INSERT INTO STATION
VALUES(
    'S100','MADURAI'
);
COMMIT;
INSERT INTO STATION 
VALUES(
    'S101','DINDIGUL'
);

INSERT INTO STATION 
VALUES(
    'S102','TRICHY'
);

INSERT INTO STATION 
VALUES(
    'S103','SRIRANGAM'
);

INSERT INTO STATION 
VALUES(
    'S104','ARIYALLUR'
);

INSERT INTO STATION 
VALUES(
    'S105','VRIDACHALLAM'
);

INSERT INTO STATION 
VALUES(
    'S106','VILLUPURAM'
);

INSERT INTO STATION
VALUES(
    'S107','CHENGALPATTU'
);

INSERT INTO STATION 
VALUES(
    'S108','TAMBARAM'
);

INSERT INTO STATION 
VALUES(
    'S109','CHENNAI_EGMORE'
);
commit;
  

INSERT INTO  Schedule
VALUES(
    'SC100','T100','S100','NA','6:40 am'
);
commit;


INSERT INTO Schedule
VALUES(
    'SC101','T100','S101','7:30 am ','7:35 am'
);
INSERT INTO Schedule
VALUES(
    'SC102','T100','S102',' 9:00 am ','9:15 am'
);

INSERT INTO Schedule
VALUES(
    'SC103','T100','S103','10:00 am','10:03 am'
);

INSERT INTO Schedule
VALUES(
    'SC104','T100','S104','10:30 am','10:33 am'
);

INSERT INTO Schedule
VALUES(
    'SC105','T100','S105','11:00 am','11:05 am'
);

INSERT INTO Schedule
VALUES(
    'SC106','T100','S106','12:00 am','12:05 pm'
);

INSERT INTO Schedule
VALUES(
    'SC107','T100','S107','12:45 pm','12:50 pm'
);

INSERT INTO Schedule
VALUES(
    'SC108','T100','S108','13:20 pm','13:25 pm'
);

INSERT INTO Schedule
VALUES(
    'SC109','T100','S109','13:55 pm','NA'
);
INSERT INTO Schedule
VALUES(
    'SC110','T100','S102','7:30 am ','9:00 am'
);
INSERT INTO Schedule
VALUES(
    'SC111','T100','S103','7:30 am ','10:00 am'
);

INSERT INTO Schedule
VALUES(
    'SC112','T100','S104','7:30 am ','10:30 am'
);

INSERT INTO Schedule
VALUES(
    'SC113','T100','S105','7:30 am ','11:00 am'
);

INSERT INTO Schedule
VALUES(
    'SC114','T100','S106','7:30 am ','12:00 am'
);

INSERT INTO Schedule
VALUES(
    'SC115','T100','S107','7:30 am ','12:45 pm'
);

INSERT INTO Schedule
VALUES(
    'SC116','T100','S108','7:30 am ','13:20 pm'
);
INSERT INTO Schedule
VALUES(
    'SC117','T100','S109','7:30 am ','13:55 pm'
);

INSERT INTO Schedule
VALUES(
    'SC118','T100','S103','9:00 am ','10:00 am'
);


INSERT INTO Schedule
VALUES(
    'SC119','T100','S104','9:00 am ','10:30 am'
);

INSERT INTO Schedule
VALUES(
    'SC120','T100','S105','9:00 am ','11:00 am'
);

INSERT INTO Schedule
VALUES(
    'SC121','T100','S106','9:00 am ','12:00 am'
);
INSERT INTO Schedule
VALUES(
    'SC122','T100','S107','9:00 am ','12:45 pm'
);
INSERT INTO Schedule
VALUES(
    'SC123','T100','S108','9:00 am ','13:20 pm'
);
INSERT INTO Schedule
VALUES(
    'SC124','T100','S109','9:00 am ','13:55 pm'
);

INSERT INTO Schedule
VALUES(
    'SC125','T100','S104','10:00 am ','10:30 am'
);

INSERT INTO Schedule
VALUES(
    'SC126','T100','S105','10:00 am ','11:00 am'
);
INSERT INTO Schedule
VALUES(
    'SC127','T100','S106','10:00 am ','12:00 am'
);
INSERT INTO Schedule
VALUES(
    'SC128','T100','S107','10:00 am ','12:45 pm'
);
INSERT INTO Schedule
VALUES(
    'SC129','T100','S108','10:00 am ','13:20 pm'
);
INSERT INTO Schedule
VALUES(
    'SC130','T100','S109','10:00 am ','13:55 pm'
);

INSERT INTO Schedule
VALUES(
    'SC131','T100','S105','10:30 am ','11:00 am'
);


INSERT INTO Schedule
VALUES(
    'SC132','T100','S106','10:30 am ','12:00 am'
);


INSERT INTO Schedule
VALUES(
    'SC133','T100','S107','10:30 am ','12:45 pm'
);

INSERT INTO Schedule
VALUES(
    'SC134','T100','S108','10:30 am ','13:20 pm'
);
INSERT INTO Schedule
VALUES(
    'SC135','T100','S109','10:30 am ','13:55 pm'
);

INSERT INTO Schedule
VALUES(
    'SC136','T100','S106','11:00 am ','12:00 pm'
);

INSERT INTO Schedule
VALUES(
    'SC137','T100','S107','11:00 am ','12:45 pm'
);
INSERT INTO Schedule
VALUES(
    'SC138','T100','S108','11:00 am ','13:20 pm'
);

INSERT INTO Schedule
VALUES(
    'SC139','T100','S109','11:00 am ','13:55 pm'
);
INSERT INTO Schedule
VALUES(
    'SC140','T100','S107','12:00 am ','12:45 pm'
);
INSERT INTO Schedule
VALUES(
    'SC141','T100','S108','12:00 am ','13:20 pm'
);
INSERT INTO Schedule
VALUES(
    'SC142','T100','S109','12:00 am ','13:55 pm'
);
INSERT INTO Schedule
VALUES(
    'SC143','T100','S108','12:45 am ','13:20 pm'
);
INSERT INTO Schedule
VALUES(
    'SC144','T100','S109','12:45 am ','13:55 pm'
);
INSERT INTO Schedule
VALUES(
    'SC145','T100','S109','13:20 pm ','13:55 pm'
);


COMMIT;


INSERT INTO Ticket
VALUES(
    'TK01','T100','SC101','S100','S101','200'
);

INSERT INTO Ticket
VALUES(
    'TK02','T100','SC101','S100','S101','200'
);

INSERT INTO Ticket
VALUES(
    'TK03','T100','SC101','S100','S101','200'
);

INSERT INTO Ticket
VALUES(
    'TK04','T100','SC102','S100','S102','80'
);

INSERT INTO Ticket
VALUES(
    'TK05','T100','SC102','S100','S102','80'
);

INSERT INTO Ticket
VALUES(
    'TK06','T100','SC103','S100','S103','50'
);

INSERT INTO Ticket
VALUES(
    'TK07','T100','SC104','S100','S104','50'
);

INSERT INTO Ticket
VALUES(
    'TK08','T100','SC105','S100','S105','50'
);

INSERT INTO Ticket
VALUES(
    'TK09','T100','SC106','S100','S106','50'
);

INSERT INTO Ticket
VALUES(
    'TK10','T100','SC107','S100','S107','50'
);
INSERT INTO Ticket
VALUES(
    'TK11','T100','SC108','S100','S108','50'
);

INSERT INTO Ticket
VALUES(
    'TK12','T100','SC109','S100','S109','50'
);
INSERT Into Ticket 
Values('TK50','T100','SC111','S101','S103','50'
);
INSERT INTO Ticket
Vaues('TK60','T100','SC112','S101','S104','40'

);
INSERT INTO Ticket
Values('TK70','T100','SC113','S101','S105','20'
);
INSERT INTO Ticket
VALUES(
    'TK80','T100','SC114','S101','S106','20'
);
INSERT INTO Ticket
VALUES(
    'TK90','T100','SC115','S101','S107','20'
);
INSERT INTO Ticket
VALUES(
    'TK100','T100','SC116','S101','S108','20'
);
INSERT INTO Ticket
VALUES(
    'TK110','T100','SC117','S101','S109','20'
);


INSERT Into Ticket 
Values('TK51','T100','SC118','S102','S103','50'
);


INSERT INTO Ticket
Vaues('TK61','T100','SC119','S102','S104','40'

);
INSERT INTO Ticket
Values('TK71','T100','SC120','S102','S105','20'
);


INSERT INTO Ticket
VALUES(
    'TK81','T100','SC121','S102','S106','20'
);

INSERT INTO Ticket
VALUES(
    'TK91','T100','SC122','S102','S107','20'
);
INSERT INTO Ticket
VALUES(
    'TK101','T100','SC123','S102','S108','20'
);

INSERT INTO Ticket
VALUES(
    'TK111','T100','SC124','S102','S109','20'
);
INSERT INTO Ticket
Values('TK62','T100','SC125','S103','S104','20'

);

INSERT INTO Ticket
Values('TK72','T100','SC126','S103','S105','20'
);

INSERT INTO Ticket
VALUES(
    'TK82','T100','SC127','S103','S106','20'
);
INSERT INTO Ticket
VALUES(
    'TK92','T100','SC128','S103','S107','20'
);

INSERT INTO Ticket
VALUES(
    'TK102','T100','SC129','S103','S108','20'
);

INSERT INTO Ticket
VALUES(
    'TK112','T100','SC130','S103','S109','20'
);


INSERT INTO Ticket
VALUES('TK73','T100','SC131','S104','S105','20'

);

INSERT INTO Ticket
VALUES(
    'TK83','T100','SC132','S104','S106','20'
);

INSERT INTO Ticket
VALUES(
    'TK93','T100','SC133','S104','S107','20'
);

INSERT INTO Ticket
VALUES(
    'TK103','T100','SC134','S104','S108','20'
);

INSERT INTO Ticket
VALUES(
    'TK113','T100','SC135','S104','S109','20'
);


INSERT INTO Ticket
VALUES(
    'TK84','T100','SC136','S105','S106','20'
);



INSERT INTO Ticket
VALUES(
    'TK94','T100','SC137','S105','S107','20'
);
INSERT INTO Ticket
VALUES(
    'TK104','T100','SC138','S105','S108','20'
);

INSERT INTO Ticket
VALUES(
    'TK114','T100','SC139','S105','S109','20'
);


INSERT INTO Ticket
VALUES(
    'TK96','T100','SC140','S106','S107','20'
);




INSERT INTO Ticket
VALUES(
    'TK105','T100','SC141','S106','S108','20'
);

INSERT INTO Ticket
VALUES(
    'TK115','T100','SC142','S106','S109','20'
);
INSERT INTO Ticket
VALUES(
    'TK106','T100','SC143','S107','S108','20'
);
INSERT INTO Ticket
VALUES(
    'TK116','T100','SC144','S107','S109','20'
);
INSERT INTO Ticket
VALUES(
    'TK117','T100','SC145','S108','S109','20'
);











INSERT INTO Cost
VALUES(
    'TK01','T100','S100','S101',500
);
INSERT INTO Cost
VALUES(
    'TK02','T100','S100','S101',500
);

INSERT INTO Cost
VALUES(
    'TK03','T100','S100','S101',500
);

INSERT INTO Cost
VALUES(
    'TK04','T100','S100','S102',430
);

INSERT INTO Cost
VALUES(
    'TK05','T100','S100','S102',430
);

INSERT INTO Cost
VALUES(
    'TK06','T100','S100','S103',400
);


INSERT INTO Cost
VALUES(
    'TK07','T100','S100','S104',350
);

INSERT INTO Cost
VALUES(
    'TK08','T100','S100','S105',320
);


INSERT INTO Cost
VALUES(
    'TK09','T100','S100','S106',300
);
INSERT Into Cost 
Values('TK50','T100','S101','S103',300
);

INSERT Into COST
Values('TK51','T100','S102','S103',300
);
INSERT INTO COST
Values('TK60','T100','S101','S104',300

);
INSERT INTO COST
Values('TK61','T100','S102','S104',300

);

INSERT INTO COST
Values('TK62','T100','S103','S104',200

);

INSERT INTO COST
Values('TK70','T100','S101','S105',300
);
INSERT INTO COST
Values('TK71','T100','S102','S105',300
);
INSERT INTO COST
Values('TK72','T100','S103','S105',250
);
INSERT INTO COST 
VALUES('TK73','T100','S104','S105',200

);
INSERT INTO Cost
VALUES(
    'TK80','T100','S101','S106',300
);
INSERT INTO Cost
VALUES(
    'TK81','T100','S102','S106',300
);
INSERT INTO Cost
VALUES(
    'TK82','T100','S103','S106',300
);

INSERT INTO Cost
VALUES(
    'TK83','T100','S104','S106',300
);
INSERT INTO Cost
VALUES(
    'TK84','T100','S105','S106',300
);


INSERT INTO Cost
VALUES(
    'TK10','T100','S100','S107',300
);



INSERT INTO Cost
VALUES(
    'TK11','T100','S100','S108',300
);
INSERT INTO Cost
VALUES(
    'TK12','T100','S100','S109',300
);
INSERT INTO Cost
VALUES(
    'TK90','T100','S101','S107',300
);
INSERT INTO Cost
VALUES(
    'TK91','T100','S102','S107',300
);

INSERT INTO Cost
VALUES(
    'TK92','T100','S103','S107',300
);

INSERT INTO Cost
VALUES(
    'TK93','T100','S104','S107',300
);

INSERT INTO Cost
VALUES(
    'TK94','T100','S105','S107',300
);

INSERT INTO Cost
VALUES(
    'TK96','T100','S106','S107',300
);


INSERT INTO Cost
VALUES(
    'TK100','T100','S101','S108',300
);

INSERT INTO Cost
VALUES(
    'TK101','T100','S102','S108',300
);

INSERT INTO Cost
VALUES(
    'TK102','T100','S103','S108',300
);

INSERT INTO Cost
VALUES(
    'TK103','T100','S104','S108',300
);

INSERT INTO Cost
VALUES(
    'TK104','T100','S104','S108',300
);

INSERT INTO Cost
VALUES(
    'TK105','T100','S105','S108',300
);

INSERT INTO Cost
VALUES(
    'TK106','T100','S106','S108',300
);

INSERT INTO Cost
VALUES(
    'TK107','T100','S107','S108',300
);








INSERT INTO Cost
VALUES(
    'TK110','T100','S101','S109',300
);

INSERT INTO Cost
VALUES(
    'TK111','T100','S102','S109',300
);

INSERT INTO Cost
VALUES(
    'TK112','T100','S103','S109',300
);

INSERT INTO Cost
VALUES(
    'TK113','T100','S104','S109',300
);

INSERT INTO Cost
VALUES(
    'TK114','T100','S105','S109',300
);
INSERT INTO Cost
VALUES(
    'TK115','T100','S106','S109',300
);

INSERT INTO Cost
VALUES(
    'TK116','T100','S107','S109',300
);

INSERT INTO Cost
VALUES(
    'TK117','T100','S108','S109',300
);



INSERT Into COST
Values('TK50','T100','S101','S103',250
);
INSERT Into COST
Values('TK51','T100','S102','S103',250
);










commit;