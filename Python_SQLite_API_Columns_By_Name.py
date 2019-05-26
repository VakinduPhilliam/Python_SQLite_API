# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Accessing columns by name instead of by index.
# One useful feature of the sqlite3 module is the built-in sqlite3.Row class designed to be used as a row factory.
# Rows wrapped with this class can be accessed both by index (like tuples) and case-insensitively by name:
 
import sqlite3

con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row

cur = con.cursor()
cur.execute("select 'John' as name, 42 as age")

for row in cur:

    assert row[0] == row["name"]
    assert row["name"] == row["nAmE"]

    assert row[1] == row["age"]
    assert row[1] == row["AgE"]
