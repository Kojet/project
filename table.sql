CREATE TABLE book(
bid varchar(10) PRIMARY key,
name varchar(20) NOT NULL, 
author varchar(20) NOT NULL, 
type varchar(10) NOT NULL, 
price varchar(5) NOT NULL);

CREATE TABLE user (
uid varchar(10) PRIMARY KEY,
password varchar(10) NOT NULL, 
job varchar(1) NOT NULL );

CREATE TABLE borrow (bid varchar(10) PRIMARY KEY,  
uid varchar(10) NOT NULL, 
date datetime NOT NULL,
FOREIGN KEY (bid) REFERENCES book(bid),
FOREIGN KEY (uid) REFERENCES user(uid));