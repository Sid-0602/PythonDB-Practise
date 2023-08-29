import psycopg2, sys, os
f = open('./player.txt','r')
name = f.read()
#name = name + "%" query for like 


database = 'flis'
user = 'postgres'
password = '************'
port = '5432'
host = 'localhost'

conn = None
try:
    conn = psycopg2.connect(database=database,user=user,password=password,port=port,host=host)
    cur = conn.cursor()
    cur.execute("select name from players where name =%s",(name,))
    #query for is Like : 
    # cur.execute("select name from players where name like %s ",(name,))
    result = cur.fetchall()
    for i in result:
        print(i[0])
    cur.close()
except(Exception,psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
