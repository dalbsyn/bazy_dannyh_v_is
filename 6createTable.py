DB_PARAMS= {
       "dbname" = "postgres"
       "user" = "postgres"
       "password" = "bliss149bliss"
       "host" = "localhost"
       "port" = "5432"
def createTable ():
      conn = psycora2.connect(**DB_PARAMS)
      cur = conn.cursor()

     cur.execute("""
           CREATE TABLE owners (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            birth_date DATE NOT NULL

           )
""")

     cur.execute("""
           CREATE TABLE cars (
           id SERIAL PRIMARY KEY,
           owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
           brand VARCHAR(100),
           model VARCHAR(100),
           year INT
           )
""")
  conn.commit()
  cur.close()
  conn.close()
}
If __name__="__main__":
     createTable()