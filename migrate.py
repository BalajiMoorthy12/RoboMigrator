from pymongo import MongoClient
import datetime 
from datetime import date
import psycopg2
def encode_date(value):
    return datetime.datetime.combine(
            value,
            datetime.datetime.min.time())
def transform_incoming(doc):
    for (key, value) in doc.items():
        if type(value) == datetime.date:
            doc[key] = encode_date(value)
    return (doc)
def migrate(table,columns,data_list):
    client = MongoClient('localhost', 27017)
    db = client['MyMongo']
    collection=db[table]
    doc={}
    for i in data_list:
        #print(i)
        for column,data in zip(columns,i):doc[column]=data
        if '_id' in doc: del doc['_id']
        doc2 = transform_incoming(doc)
        collection.insert_one(doc2)
    return (collection.count())
    #print(table +" table inserted successfully in Mongo")
def postgresql_db(passw,user1):
    conn = psycopg2.connect(database='dbname', user = user1, password = passw, host = "127.0.0.1", port = "5432")
    print("Opened database successfully")
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur2.execute("""SELECT table_name
      FROM information_schema.tables
     WHERE table_schema='public'
       AND table_type='BASE TABLE';""")
    column = []
    datatype = []
    det=[]
    tabletemp=[]
    table_rows=cur2.fetchall()
    for table in table_rows:
        query=("SELECT * FROM  information_schema.COLUMNS"
                    " WHERE table_name = '{}'").format(str(table[0]))
        cur.execute(query)
        rows = cur.fetchall()
        column = []
        datatype = []
        for row in rows:
            column.append(row[3])
            datatype.append(row[7])
        query=("SELECT * FROM ""{}""").format(str(table[0]))
        cur.execute(query)
        rows2 = cur.fetchall()
        #print(len(rows2),str(table[0]))
        mong_count=migrate(str(table[0]),column,rows2)
        if mong_count == len(rows2): print(("Total {} records from PostgreSQL table {} is migrated successfully to {} in mongo as collection").format(mong_count,str(table[0]),str(table[0])))
    print("Operation done successfully")
    conn.commit()
    print("Records created successfully")
    conn.close()
#print(postgresql_db('balaji1212', 'dbname', 'postgres'))

def postgresql_onlydb(db):
    conn = psycopg2.connect(database=db, user = 'postgres', password = 'balaji1212', host = "127.0.0.1", port = "5432")
    print("Opened database successfully")
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur2.execute("""SELECT table_name
      FROM information_schema.tables
     WHERE table_schema='public'
       AND table_type='BASE TABLE';""")
    column = []
    datatype = []
    det=[]
    tabletemp=[]
    table_rows=cur2.fetchall()
    for table in table_rows:
        query=("SELECT * FROM  information_schema.COLUMNS"
                    " WHERE table_name = '{}'").format(str(table[0]))
        cur.execute(query)
        rows = cur.fetchall()
        column = []
        datatype = []
        for row in rows:
            column.append(row[3])
            datatype.append(row[7])
        query=("SELECT * FROM ""{}""").format(str(table[0]))
        cur.execute(query)
        rows2 = cur.fetchall()
        print(len(rows2),str(table[0]))
        det.append(len(rows2))
        tabletemp.append(str(table[0]))
    #print(det,tabletemp)
        mongo_count=migrate(str(table[0]),column,rows2)
        if mongo_count == len(rows2):   
            print(("{} records are successfully migrated from {} to Mongo collection {}").format(mongo_count,(str(table[0])),(str(table[0]))))    
    print("Operation done successfully")
    conn.commit()
    print("Records created successfully")
    conn.close()
    return tabletemp,det
#print(postgresql_db('balaji1212', 'dbname', 'postgres'))