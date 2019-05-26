# Python SQLite API
# sqlite3 � DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn�t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It�s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Converting SQLite values to custom Python types.
# Writing an adapter lets you send custom Python types to SQLite.
# Enter converters.
# Let�s go back to the Point class. We stored the x and y coordinates separated via semicolons as strings in SQLite.
# First, we�ll define a converter function that accepts the string as a parameter and constructs a Point object from it.
# 
# Note:
# Converter functions always get called with a bytes object, no matter under which data type you sent the value to SQLite.
# 

def convert_point(s):
    x, y = map(float, s.split(b";"))

    return Point(x, y)

# 
# Now you need to make the sqlite3 module know that what you select from the database is actually a point.
# There are two ways of doing this:
# > Implicitly via the declared type
# > Explicitly via the column name
#
# Both ways are described in section Module functions and constants, in the entries for the constants PARSE_DECLTYPES and PARSE_COLNAMES.
# 
# The following example illustrates both approaches.
# 

import sqlite3

class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "(%f;%f)" % (self.x, self.y)

def adapt_point(point):
    return ("%f;%f" % (point.x, point.y)).encode('ascii')

def convert_point(s):
    x, y = list(map(float, s.split(b";")))

    return Point(x, y)

# Register the adapter

sqlite3.register_adapter(Point, adapt_point)

# Register the converter

sqlite3.register_converter("point", convert_point)

p = Point(4.0, -3.2)

#########################

# 1) Using declared types

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)

cur = con.cursor()
cur.execute("create table test(p point)")

cur.execute("insert into test(p) values (?)", (p,))
cur.execute("select p from test")

print("with declared types:", cur.fetchone()[0])

cur.close()

con.close()

#######################

# 2) Using column names

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)

cur = con.cursor()
cur.execute("create table test(p)")

cur.execute("insert into test(p) values (?)", (p,))
cur.execute('select p as "p [point]" from test')

print("with column names:", cur.fetchone()[0])

cur.close()
con.close()
