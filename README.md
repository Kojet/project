## Operating systems
Linux for MySQL server.
Windows 10 / Linux for main program.
## Main Program
#### Programming Language
Base on python(for the GUI and back-end part),  the retrieving part is written by SQL.
#### Library used
tkinter, pymysql

## Deploying Procedure
We deploy the MySQL in the Alibaba Cloud Server. So firstly, we need to use SSH to login our cloud server. And We have pre-configured remote access of the MySQL.
Check if the MySQL is active.
```
sudo netstat -tap | grep mysql
```
Back to the local terminal, check whether we can connect to the MySQL remotely.
```
mysql -uvisitor -p1234 -h 120.79.31.91
```
Build database and table.
```
create database library;
use library;

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
```
Next, run the main program in local.
```
python3 initial.py
```