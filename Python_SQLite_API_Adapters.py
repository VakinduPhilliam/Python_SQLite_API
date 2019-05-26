# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
#
# Using adapters to store additional Python types in SQLite databases.
# Letting your object adapt itself.
#
 
#
# Let’s suppose you have a class like this:
# 

class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y
 
#
# Now you want to store the point in a single SQLite column. First you’ll have to choose one of the supported types first to be used for
# representing the point. Let’s just use str and separate the coordinates using a semicolon.
# Then you need to give your class a method __conform__(self, protocol) which must return the converted value.
# The parameter protocol will be PrepareProtocol.
# 

import sqlite3

class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __conform__(self, protocol):

        if protocol is sqlite3.PrepareProtocol:
            return "%f;%f" % (self.x, self.y)

con = sqlite3.connect(":memory:")

cur = con.cursor()

p = Point(4.0, -3.2)

cur.execute("select ?", (p,))

print(cur.fetchone()[0])
