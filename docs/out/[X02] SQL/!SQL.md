<link rel="stylesheet" href="../../stylesheet.css">

# SQL Syntax

## RDBMS
**RDBMS** stands for *Relational Database Management System*. **RDBMS** is the basis for **SQL**, and for all modern database systems such as **MS SQL Server**, **IBM DB2**, **Oracle**, **MySQL**, and **Microsoft Access**.

## DATA TYPES
### Strings
| Data type                       | Description                                            |
|---------------------------------|--------------------------------------------------------|
| `CHAR(size)`                    | *A FIXED length string;* `size[0-255](default=1)`      |
| `VARCHAR(size)`                 | *A VARIABLE length string;* `size[0-65535]`            |
| `TEXT(size)`                    | *Holds a string with a maximum length of 65,535 bytes* |
| `ENUM(val1, val2, val3, ...)`   | *A string object that can have only one value, chosen from a list of possible values.* |
| `SET(val1, val2, val3, ...)`    | *A string object that can have 0 or more values, chosen from a lis²t of possible values. You can list up to 64 values in a SET list.* |

### Numerics
| Data type               | Description                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------|
| `BIT(size)`             | *A bit-value type.* `size[1-64](default=1)`                                                |
| `BOOL` / `BOOLEAN`      | *Zero is considered as false, nonzero values are considered as true.*                      |
| `INT` / `INTEGER(size)` | `size` *- specifies the maximum display width (which is 255)*                              |
| `FLOAT(p)`              | `p` *- value to determine whether to use `FLOAT` or `DOUBLE` for the resulting data type.* |


# MySQL Requests
## Database Management

### Display Databases
```sql
SHOW DATABASES;
```

### Create DB
```sql
CREATE DATABASE db_name;
```

### Delete DB
```sql
DROP DATABASE db_name;
```

### Execute .sql on a database
```sh
mysql -u root -p db_name_to_operate_on < requests.sql
```

### Display user's grants
```sql
SHOW GRANTS FOR 'user'@'localhost'
```

### Create new user
```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
```

### List all users
```sql
SELECT user, host FROM mysql.user;
```

### Alter user's password
```sql
ALTER USER 'user'@'localhost' IDENTIFIED BY 'new_password';
```

### Grant Privileges
```sql
GRANT ALL PRIVILEGES ON your_database.* TO 'new_user'@'localhost';
FLUSH PRIVILEGES;
```

### Make database read-only
```sql
ALTER DATABASE db_name READ ONLY = 1;
```
> If a database is read only, then it cannot be dropped.



## Table Operations
### Display tables
```sql
SHOW TABLES;
```

### Display columns
```sql
SHOW columns FROM table;
```

### New table
```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
);
```

### Insert row(s) into a table
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES
    (value11, value12, ..., value1M)
    (value21, value22, ..., value2M)
    ...
    (valueN1, valueN2, ..., valueNM)
    ;
```

### Delete row(s) from a table
```sql
DELETE FROM table_name WHERE id = '1';
```

```sql
DELETE FROM table_name;
```

### Rename table
```sql
RENAME TABLE table_to_rename TO new_name;
```

### Update table
```sql
UPDATE table_name SET column_name = <value> WHERE <condition>
```


## Searching

### Select columns
```sql
SELECT column1, column2, ...
FROM table_name;
```

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```


### Conditions
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

> The following operators can be used in the `WHERE` clause:

| Operator  | Description                          |
|-----------|--------------------------------------|
| `=`       | Equal                                |
| `>`, `>=` | Greater (equal) than                 |
| `<`, `<=` | Less (equal) than                    |
| `<>`      | Not equal                            |
| `BETWEEN` | Range                                |
| `LIKE`    | Search for a pattern                 |
| `IN`      | List of possible values for a column |

