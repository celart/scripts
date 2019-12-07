

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

