# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# connection. 
# This read-only attribute provides the SQLite database Connection used by the Cursor object.
# A Cursor object created by calling con.cursor() will have a connection attribute that refers to con:

con = sqlite3.connect(":memory:")

cur = con.cursor()
cur.connection == con

#
# OUTPUT:
#
# True
#
