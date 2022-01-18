# Inventory Application

This repository provides a python web application which loads/retrieves inventory records into/from database.

Application Structure:- \
The application is made up of 3 components
1) Flask application - a rest service to allow users to insert or delete records
2) Database - a mysql database to store inventory records
3) SQLalchemy ORM - an interface to read/write records from/to database.


Mysql can be installed on respective operating system from below link \
https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/

To install python (v3.8.2), refer to the below link (preferred version 3.8.2) \ 
https://realpython.com/installing-python/

**Installation guide** :-
1) Run `pip install -r requirements.txt` to install dependencies. 
2) To store records in mysql, a running mysql instance is needed. Login to the mysql instance and execute below command
`create database <database_name>` \
This is needed to allow ORM to connect to database.
3) Update `config/config.py` with mysql configs\
The fields to be updated are\
`mysql_user, mysql_password, mysql_host, mysql_port, database, inventory_table(name of the table to be created- Ex-"inventory_table"`.
4) Run `python3 create_table.py dev` to create the inventory table in dev environment. Use `test` only to run test_cases.
5) At this point, all the setup is complete, run `python3 start.py dev` to start application.

By default, the application is started on url `http://localhost:8080/`. 
To host the application on a server and access remotely,
update `config/config.py` to set `application_host = "0.0.0.0"` and access the application using `http://<server_ip>:<port_no>/`

To run test cases, update test configs in `config/config.py` and execute `coverage run -m unittest test/test_cases.py`  
To view code coverage, run `coverage report -m`  


**Sample Requests**
1) Insert a record - \
    `curl --request POST --data '{"id" : 1, "name" : "inventory_test", "cost" : 100 , "location" : "test_location"}' http://127.0.0.1:8080/inventory`   
2) Retrieve a record - \
    `curl --request GET  --data '{"id" : 1}' http://127.0.0.1:8080/inventory`
3) Retrieve all records - \
    `curl --request GET http://127.0.0.1:8080/inventory/all`
4) Update a record - \
    `curl --request PUT --data '{"id" : 1, "name" : "inventory_test_update", "cost" : 111 }' http://127.0.0.1:8080/inventory`
5) Delete a record - \
    `curl --request DELETE --data '{"id" : 1, "deletion_comments" : "Deleting record 1"}' http://127.0.0.1:8080/inventory`
6) Restore a record - \
    `curl --request PUT --data '{"id" : 1}' http://127.0.0.1:8080/inventory/undo`