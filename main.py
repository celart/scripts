import nodes
import re
import nlisLoad
import nlisTermLoad
import dbConnector
import sqlite3

nTarget=nlisLoad.parse("NLIST.lis")
nTerm=nlisTermLoad.parse("ScalarLayer0.txt")

conn = sqlite3.connect("db.sqlite")
dbConnector.createDb(conn)
dbConnector.insertTNode(conn, nTarget)
dbConnector.insertCNode(conn, nTerm)
#print(len(f))
