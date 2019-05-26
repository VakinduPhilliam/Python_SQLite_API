# Python SQLite API
# sqlite3 � DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn�t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It�s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# 
# The sqlite3 module has two default adapters for Python�s built-in datetime.date and datetime.datetime types. 
# Now let�s suppose we want to store datetime.datetime objects not in ISO representation, but as a Unix timestamp.
# 

import sqlite3
import datetime
import time

def adapt_datetime(ts):
    return time.mktime(ts.timetuple())

sqlite3.register_adapter(datetime.datetime, adapt_datetime)

con = sqlite3.connect(":memory:")

cur = con.cursor()

now = datetime.datetime.now()

cur.execute("select ?", (now,))

print(cur.fetchone()[0])
