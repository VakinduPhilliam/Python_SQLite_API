# Python DBM
# dbm � Interfaces to Unix �databases�
# dbm is a generic interface to variants of the DBM database � dbm.gnu or dbm.ndbm.
# If none of these modules is installed, the slow-but-simple implementation in module dbm.dumb will be used.
# There is a third party interface to the Oracle Berkeley DB.
#
# The following example records some hostnames and a corresponding title, and then prints out the contents of
# the database:
# 

import dbm

# Open database, creating it if necessary.

with dbm.open('cache', 'c') as db:

    # Record some values

    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    # Note that the keys are considered bytes now.

    assert db[b'www.python.org'] == b'Python Website'

    # Notice how the value is now in bytes.

    assert db['www.cnn.com'] == b'Cable News Network'

    # Often-used methods of the dict interface work too.

    print(db.get('python.org', b'not present'))

    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError).

    db['www.yahoo.com'] = 4

# db is automatically closed when leaving the with statement.
