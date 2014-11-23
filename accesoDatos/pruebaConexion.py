#sudo apt-get install python-psycopg2

import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=mytestdb user=bryanstm")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO Actor (id, nombre, pais) VALUES (%s, %s, %s)",
    (1027, "Stiven Tabarez", "Colombia"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM Actor;")
cur.fetchone()
#(1, 100, "abc'def")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

print("PRUEBA CONEXION")