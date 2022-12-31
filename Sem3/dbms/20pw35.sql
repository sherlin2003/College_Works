drop table sailor;
drop table boat;

create table sailor ( sid INT PRIMARY KEY,  name VARCHAR(90) , rating int , age int,
check(rating >=6 and rating <=10));
 insert into sailor values( 1 , 'jack sparrow',10,40);
 insert into sailor values (2,'Will Turner', 6, 26);
 insert into Sailor values (3,'Horatio', 7, 24);
 insert into Sailor values (4,' Gibbs ', 9, 51); 
 insert into Sailor  values (5,'Davey Jones', 10, 42);
 insert into Sailor values (6,'Julius',9, 25);
insert into Sailor  values (7, 'Dustin', 7, 45);
insert into Sailor values (8, 'Rusty', 10, 35);
insert into Sailor  values (9, 'Horatio', 6, 35);
insert into Sailor  values (10, 'Zorba', 8, 18);
insert into Sailor  values (11, 'Julius',9, 25);

 select * from sailor;
 
create table boat (bid INT PRIMARY KEY,  name VARCHAR(90), colour varchar(10) ); 
insert into Boat values (101, 'Interlake', 'blue');
insert into Boat values (102, 'Interlake', 'red');
insert into Boat values (103, 'Clipper', 'green');
insert into Boat values (104, 'Marine', 'red');
insert into Boat values (105,'Black Pearl', 'black');
insert into Boat values (106,'Queen Annes Revenge', 'red');
insert into Boat values (107,'Blackbeards Delight', 'black');
insert into Boat values (108,'Redbeards Delight', 'red');
insert into Boat values (109,'Oceans Dagger', 'blue');
insert into Boat values (110,'Marine', 'blue');
insert into Boat values(111,'Interlake', 'red');

select * from boat;

drop table Reservation;

create table Reservation ( sid int , bid int , day date, foreign key (sid)references sailor(sid) ,
foreign key (bid) references boat(bid)); 

insert into Reservation values (2, 101,'11-FEB-2016'); 
insert into Reservation values (6, 107,'10-JUN-2016');
insert into Reservation values (1, 101,'10-OCT-2016'); 
insert into Reservation values (1, 101, '10-OCT-2017');
insert into Reservation values (1, 102, '10-OCT-2017');
insert into Reservation values (1, 101, '10-JUL-2017');
insert into Reservation values (2, 102, '11-SEP-2017');
insert into Reservation values (2, 102, '7-NOV-2017');
insert into Reservation values (3, 101, '7-NOV-2017');
insert into Reservation values (3, 102, '7-AUG-2017');
insert into Reservation values (4, 103, '19-SEP-2017');
insert into Reservation values (6, 104, '19-SEP-2017');
select * from reservation;

select count(*) as no_of_black_boats from boat where colour='black';
select distinct(s.sid) , s.name from sailor s , boat b , reservation r  where s.sid=r.sid and b.bid=r.bid and colour='red' or colour='green';
select name as Name from sailor where age=(select min(age) from sailor);
select distinct s.* from reservation r , sailor s , boat b where ( s.sid=r.sid and b.bid=r.bid and b.bid =101);
select distinct(b.colour) from boat b , sailor s , reservation r where r.sid=s.sid and r.bid=b.bid and s.name= 'Horatio' ;
select count(*) from boat b , sailor s , reservation r where r.sid=s.sid and r.bid=b.bid and colour='red' and rating=10;
select name from sailor where sid not in ( select sid from reservation);
