# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# sqlite3.complete_statement(sql). 
# Returns True if the string sql contains one or more complete SQL statements terminated by semicolons.
# It does not verify that the SQL is syntactically correct, only that there are no unclosed string literals and the statement is terminated
# by a semicolon.

#
# This can be used to build a shell for SQLite, as in the following example:
# A minimal SQLite shell example
#

import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None

cur = con.cursor()

buffer = ""

print("Enter your SQL commands to execute in sqlite3.")
print("Enter a blank line to exit.")

while True:
    line = input()

    if line == "":
        break
    buffer += line

    if sqlite3.complete_statement(buffer):

        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print(cur.fetchall())

        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

        buffer = ""

con.close()
