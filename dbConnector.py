

def createDb(conn):
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE tNode
    (num integer PRIMARY KEY NOT NULL UNIQUE, 
    x real, 
    y real,
    z real,
    temp real)
    """)
    cur.execute("""
    CREATE TABLE cNode
    (num integer PRIMARY KEY NOT NULL UNIQUE, 
    x real, 
    y real,
    z real,
    temp real)
    """)
    cur.execute("""
    CREATE VIEW delta AS SELECT tNode.num as tNum,
cNode.num as cNum,
(cNode.x-tNode.x) AS dx,
(cNode.y-tNode.y) AS dy,
(cNode.z-tNode.z) AS dz
FROM cNode, tNode
    """)
    cur.execute("""
    CREATE VIEW cartesian AS SELECT tNum,
cNum, dx*dx+dy*dy+dz*dz as qD
FROM delta
    """)
    conn.commit()
    
def insertTNode(conn, arr):
    cur = conn.cursor()
    for i in arr:
        cur.execute("""INSERT INTO tNode
    VALUES (?, ?, ?, ?, null)""", (i.getNum(), i.getX(), i.getY(), i.getZ()))
    conn.commit() 
    
def insertCNode(conn, arr):
    cur = conn.cursor()
    for i in arr:
        cur.execute("""INSERT INTO cNode
    VALUES (?, ?, ?, ?, ?)""", (i.getNum(), i.getX(), i.getY(), i.getZ(), i.getT()))
    conn.commit() 

