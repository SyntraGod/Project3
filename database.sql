create database project3;

use project3;

create table Bus(
	num int auto_increment primary key not null,
	idBUS char(10) unique not null,
    numIn int not null,
    numOut int not null,
    timeBus date,
    statusBus int
	);
insert   into Bus (idBUS, numIn, numOut, timeBus, statusBus) values
	('0001', 10, 10, '2023-12-9', 1);
    
select * from Bus;
    
select * from Bus where idBus = '0001';

delete  from Bus

