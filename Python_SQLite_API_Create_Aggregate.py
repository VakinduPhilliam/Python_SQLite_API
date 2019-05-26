# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Connection Objects.
# create_aggregate(name, num_params, aggregate_class). 
# Creates a user-defined aggregate function.
# The aggregate class must implement a step method, which accepts the number of parameters num_params (if num_params is -1, the function
# may take any number of arguments), and a finalize method which will return the final result of the aggregate.
# The finalize method can return any of the types supported by SQLite: bytes, str, int, float and None.

import sqlite3

class MySum:

    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

con = sqlite3.connect(":memory:")
con.create_aggregate("mysum", 1, MySum)

cur = con.cursor()
cur.execute("create table test(i)")
cur.execute("insert into test(i) values (1)")

cur.execute("insert into test(i) values (2)")
cur.execute("select mysum(i) from test")

print(cur.fetchone()[0])

