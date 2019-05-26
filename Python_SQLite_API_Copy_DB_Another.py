# Python SQLite API
# sqlite3 � DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn�t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It�s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# backup(target, *, pages=0, progress=None, name="main", sleep=0.250) 
# This method makes a backup of a SQLite database even while it�s being accessed by other clients, or concurrently by the same connection.
# The copy will be written into the mandatory argument target, that must be another Connection instance.

#
# copy an existing database into another:
# 

import sqlite3

def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

con = sqlite3.connect('existing_db.db')

with sqlite3.connect('backup.db') as bck:
    con.backup(bck, pages=1, progress=progress)
