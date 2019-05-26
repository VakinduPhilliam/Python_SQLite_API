# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# text_factory. 
# Using this attribute you can control what objects are returned for the TEXT data type. By default, this attribute is set to str and the
# sqlite3 module will return Unicode objects for TEXT. If you want to return bytestrings instead, you can set it to bytes.
# You can also set it to any other callable that accepts a single bytestring parameter and returns the resulting object.

import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()

AUSTRIA = "\xd6sterreich"

# by default, rows are returned as Unicode

cur.execute("select ?", (AUSTRIA,))
row = cur.fetchone()

assert row[0] == AUSTRIA

# but we can make sqlite3 always return bytestrings ...

con.text_factory = bytes
cur.execute("select ?", (AUSTRIA,))

row = cur.fetchone()
assert type(row[0]) is bytes

# the bytestrings will be encoded in UTF-8, unless you stored garbage in the
# database ...

assert row[0] == AUSTRIA.encode("utf-8")

# we can also implement a custom text_factory ...
# here we implement one that appends "foo" to all strings

con.text_factory = lambda x: x.decode("utf-8") + "foo"
cur.execute("select ?", ("bar",))

row = cur.fetchone()
assert row[0] == "barfoo"
