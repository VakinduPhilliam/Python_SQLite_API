# Python SQLite API
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows
# accessing the database using a nonstandard variant of the SQL query language.
# Some applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
# The sqlite3 module provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# You shouldn’t assemble your query using Python’s string operations because doing so is insecure; it makes your program vulnerable to
# an SQL injection attack.
# Instead, use the DB-API’s parameter substitution. Put ? as a placeholder wherever you want to use a value, and then provide a tuple of
# values as the second argument to the cursor’s execute() method. (Other database modules may use a different placeholder, such as %s or :1.)
 
#
# Never do this -- insecure!
#

symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

#
# Do this instead
#

t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)

print(c.fetchone())

# Larger example that inserts many records at a time

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]

c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
