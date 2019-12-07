import nodes
import re
import nlisLoad
import dbConnector
import sqlite3

f=nlisLoad.parse("NLIST.lis")
conn = sqlite3.connect(":memory:")
dbConnector.createDb(conn)
dbConnector.insertTNode(conn, f)
print(len(f))
