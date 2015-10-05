# Schema Script

Use this script to turn a CSV file into an SQL script for creating tables in the altium database.  The format of the CSV should be one row per table, and the first column of each row should be the table name.  The output sql script can be executed using psql to create the tables in a database.  You need to have created the DB already.

```
psql -U postgres
CREATE DATABASE altium;
^D
python schemat2psql.py schema.csv
psql -U postgres -d altium -f schema.sql
```
