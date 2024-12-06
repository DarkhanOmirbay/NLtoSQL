import psycopg2

def execute_query(query):
    try:
        conn = psycopg2.connect(
            dbname="my_database",
            user="darkhan",
            password="password",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error executing query:",e)
        
# query = "SELECT * FROM students;"
# execute_query(query)