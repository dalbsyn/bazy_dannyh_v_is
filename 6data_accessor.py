Import psycorg 2

DB_PARAMS= {
       "dbname" = "postgres"
       "user" = "postgres"
       "password" = "bliss149bliss"
       "host" = "localhost"
       "port" = "5432"
}
def insertTable():
     conn = psycora2.connect(**DB_PARAMS)
      cur = conn.cursor()

cur.execute("""
 INSERT INTO cars (owner_id, brand, model, year) VALUES (1, 'Toyota', 'Camry', 2020);
""")

conn.commit()
cur.close()
conn.close()

}

def selectTable():
      conn = psycora2.connect(**DB_PARAMS)
      cur = conn.cursor()
      cur.execute("""
       SELECT 
      owners.name 
      cars.brand
      cars.model
FROM owners 
JOIN cars ON cars.owner_id = owners.id
""")
conn.commit()
cur.close()
conn.close()
}

if _name_ == "_main_":
  insertTable()
  selectTable()

