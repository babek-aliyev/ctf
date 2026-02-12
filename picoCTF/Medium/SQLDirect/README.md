# SQL Direct | picoCTF
## Description
Connect to this PostgreSQL server and find the flag!
## Analysis
After conneting to PostgreSQL server with given credentials, we see following output in the terminal:
```bash
┌──(kali㉿kali)-[~]
└─$ psql -h saturn.picoctf.net -p 57010 -U postgres pico
Password for user postgres: 
psql (18.1 (Debian 18.1-1), server 15.2 (Debian 15.2-1.pgdg110+1))
Type "help" for help.

pico=# 

```
As you can see now we are connected to the server and `pico=#` means PostgreSQL server expects input from us.

## Solution
To query what databases and tables we have, we can use `\d` command. When we use this command we get the following output:
```bash
pico=# \d
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)

pico=# 

```
As you can see we have `flags` relation which is `table`. That means we can see the content of this table using `select * from flags;` command. 
* `select *` selects and returns all columns from table.
* `from table` determines the table from which we want to select. In our case it is `flags`
* It is important to use `;` at the end of the expression because semicolon specifies the end of statement

## Answer
After we enter `select * from flags`, we get following output:
```bash
pico=# select * from flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{[REDACTED]}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)

pico=# 

```
