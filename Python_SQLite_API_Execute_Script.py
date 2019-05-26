# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# executescript(sql_script). 
# This is a nonstandard convenience method for executing multiple SQL statements at once. It issues a COMMIT statement first, then executes
# the SQL script it gets as a parameter.
# sql_script can be an instance of str.

import sqlite3

con = sqlite3.connect(":memory:")

cur = con.cursor()

cur.executescript("""
    create table person(
        firstname,
        lastname,
        age
    );

    create table book(
        title,
        author,
        published
    );

    insert into book(title, author, published)
    values (
        'Dirk Gently''s Holistic Detective Agency',
        'Douglas Adams',
        1987
    );
    """)
