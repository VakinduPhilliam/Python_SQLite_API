# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# executemany(sql, seq_of_parameters). 
# Executes an SQL command against all parameter sequences or mappings found in the sequence seq_of_parameters.
# The sqlite3 module also allows using an iterator yielding parameters instead of a sequence.

import sqlite3
import string

def char_generator():

    for c in string.ascii_lowercase:
        yield (c,)

con = sqlite3.connect(":memory:")

cur = con.cursor()
cur.execute("create table characters(c)")

cur.executemany("insert into characters(c) values (?)", char_generator())

cur.execute("select c from characters")

print(cur.fetchall())
