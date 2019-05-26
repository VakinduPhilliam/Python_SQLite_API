# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Default adapters and converters.
# There are default adapters for the date and datetime types in the datetime module.
# They will be sent as ISO dates/ISO timestamps to SQLite.
# The default converters are registered under the name “date” for datetime.date and under the name “timestamp” for datetime.datetime.
# This way, you can use date/timestamps from Python without any additional fiddling in most cases.
# The format of the adapters is also compatible with the experimental SQLite date/time functions.

import sqlite3
import datetime

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

cur = con.cursor()
cur.execute("create table test(d date, ts timestamp)")

today = datetime.date.today()

now = datetime.datetime.now()

cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
cur.execute("select d, ts from test")

row = cur.fetchone()

print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')

row = cur.fetchone()

print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))
