# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Using sqlite3 efficiently.
# Using shortcut methods.
# Using the nonstandard execute(), executemany() and executescript() methods of the Connection object, your code can be written more
# concisely because you don’t have to create the (often superfluous) Cursor objects explicitly.
# Instead, the Cursor objects are created implicitly and these shortcut methods return the cursor objects.
# This way, you can execute a SELECT statement and iterate over it directly using only a single call on the Connection object.
 
import sqlite3

persons = [
    ("Hugo", "Boss"),
    ("Calvin", "Klein")
    ]

con = sqlite3.connect(":memory:")

# Create the table

con.execute("create table person(firstname, lastname)")

# Fill the table

con.executemany("insert into person(firstname, lastname) values (?, ?)", persons)

# Print the table contents

for row in con.execute("select firstname, lastname from person"):
    print(row)

print("I just deleted", con.execute("delete from person").rowcount, "rows")
