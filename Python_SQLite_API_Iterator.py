# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# To retrieve data after executing a SELECT statement, you can either treat the cursor as an iterator, call the cursor’s fetchone() method
# to retrieve a single matching row, or call fetchall() to get a list of the matching rows.
# This example uses the iterator form:
 
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
