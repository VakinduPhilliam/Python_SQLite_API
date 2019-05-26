# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Cursor Objects
# class sqlite3.Cursor 
# A Cursor instance has the following attributes and methods.
# execute(sql[, parameters]) 
# Executes an SQL statement. The SQL statement may be parameterized (i. e. placeholders instead of SQL literals).
# The sqlite3 module supports two kinds of placeholders: question marks (qmark style) and named placeholders (named style).
 
import sqlite3

con = sqlite3.connect(":memory:")

cur = con.cursor()
cur.execute("create table people (name_last, age)")

who = "Yeltsin"
age = 72

# This is the qmark style:

cur.execute("insert into people values (?, ?)", (who, age))

# And this is the named style:

cur.execute("select * from people where name_last=:who and age=:age", {"who": who, "age": age})

print(cur.fetchone())
