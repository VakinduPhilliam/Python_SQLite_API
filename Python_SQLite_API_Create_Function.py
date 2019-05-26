# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Connection Objects.
# create_function(name, num_params, func). 
# Creates a user-defined function that you can later use from within SQL statements under the function name name.
# num_params is the number of parameters the function accepts (if num_params is -1, the function may take any number of arguments), and
# func is a Python callable that is called as the SQL function.
# The function can return any of the types supported by SQLite: bytes, str, int, float and None.

import sqlite3
import hashlib

def md5sum(t):
    return hashlib.md5(t).hexdigest()

con = sqlite3.connect(":memory:")
con.create_function("md5", 1, md5sum)

cur = con.cursor()
cur.execute("select md5(?)", (b"foo",))

print(cur.fetchone()[0])

