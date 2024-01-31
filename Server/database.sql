create database project3;

use project3;

create table CamInfo(
	num int auto_increment primary key not null,
	idCam char(10) unique not null,
    numIn int not null,
    numOut int not null,
    doorStatus int,
    camStatus int
	);
    
delete from caminfo;

select * from CamInfo;
    

