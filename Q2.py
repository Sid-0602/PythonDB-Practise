f= open('./name.txt')
f_name = f.read()


database = 'university'
user = 'postgres'
password = '**********'
port = '5432'
host = 'localhost'

conn = None
try: 
    conn = psycopg2.connect(database=database,user=user,password=password,port=port,host=host)
    print("Connection is Established!")

    cur = conn.cursor()
    cur.execute("select roll_no from students where student_fname= %s",(f_name,))

    result = cur.fetchall()
    for i in result:
        print(i[0])
    
    cur.close()
except(Exception,psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
