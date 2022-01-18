# Inventory Application

This repository provides a python web application which loads/retrieves inventory records into/from database.

Application Structure:- \
The application is made up of 3 components
1) Flask application - a rest service to allow users to insert or delete records
2) Database - a mysql database to store inventory records
3) SQLalchemy ORM - an interface to read/write records from/to database.


Mysql can be installed on respective operating system from below link 
https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/

To install python (v3.8.x), refer to the below link (preferred version 3.8.2)
https://realpython.com/installing-python/

**Installation guide** :-
1) Run `pip install -r requirements.txt` to install dependencies. 
2) To store records in mysql, a running mysql instance is needed. Login to the mysql instance and execute below command
`create database <database_name>` \
This is needed to allow ORM to connect to database.
3) Update `config/config.py` with mysql configs\
The fields to be updated are\
`mysql_user, mysql_password, mysql_host, mysql_port, database, inventory_table`.
4) Run `python3 create_table.py` to create the inventory table.
5) At this point, all the setup is complete, run `python3 start.py` to start application.

