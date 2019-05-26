# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Connection Objects
# create_collation(name, callable). 
# Creates a collation with the specified name and callable. The callable will be passed two string arguments.
# It should return -1 if the first is ordered lower than the second, 0 if they are ordered equal and 1 if the first is ordered higher than
# the second.
# Note that this controls sorting (ORDER BY in SQL) so your comparisons don’t affect other SQL operations.
# Note that the callable will get its parameters as Python bytestrings, which will normally be encoded in UTF-8.
 
#
# The following example shows a custom collation that sorts “the wrong way”:
# 

import sqlite3

def collate_reverse(string1, string2):

    if string1 == string2:
        return 0

    elif string1 < string2:
        return 1

    else:
        return -1

con = sqlite3.connect(":memory:")
con.create_collation("reverse", collate_reverse)

cur = con.cursor()
cur.execute("create table test(x)")

cur.executemany("insert into test(x) values (?)", [("a",), ("b",)])
cur.execute("select x from test order by x collate reverse")

for row in cur:
    print(row)

con.close()
 
#
# To remove a collation, call create_collation with None as callable:
# 

con.create_collation("reverse", None)
