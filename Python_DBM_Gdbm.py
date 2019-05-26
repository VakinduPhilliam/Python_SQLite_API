# Python DBM
# dbm — Interfaces to Unix “databases”
# dbm is a generic interface to variants of the DBM database — dbm.gnu or dbm.ndbm.
# If none of these modules is installed, the slow-but-simple implementation in module dbm.dumb will be used.
# There is a third party interface to the Oracle Berkeley DB.
# dbm.gnu — GNU’s reinterpretation of dbm
# This module is quite similar to the dbm module, but uses the GNU library gdbm instead to provide some additional
# functionality.
# Please note that the file formats created by dbm.gnu and dbm.ndbm are incompatible.
# In addition to the dictionary-like methods, gdbm objects have the following methods:
#
# gdbm.firstkey() 
# It’s possible to loop over every key in the database using this method and the nextkey() method.
# The traversal is ordered by gdbm’s internal hash values, and won’t be sorted by the key values.
# This method returns the starting key.
#
# gdbm.nextkey(key) 
# Returns the key that follows key in the traversal.
# The following code prints every key in the database db, without having to create a list in memory that contains them
# all:
 
k = db.firstkey()

while k != None:
    print(k)

    k = db.nextkey(k)
