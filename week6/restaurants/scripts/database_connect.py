## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

# import the python library for SQLite 
import cgi 
import sqlite3

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 

#insert restaurants in Xberg or Neukoelln 


db_cursor.execute("""INSERT INTO restaurants (ID,NAME,NEIGHBORHOOD_ID,PRICE_RANGE_ID)
                     VALUES ('4','Goldies','1','2')""")
db_cursor.execute("""INSERT INTO restaurants (ID,NAME,NEIGHBORHOOD_ID,PRICE_RANGE_ID)
                     VALUES ('5','Ssam ','1','2')""")
db_cursor.execute("""INSERT INTO restaurants (ID,NAME,NEIGHBORHOOD_ID,PRICE_RANGE_ID)
                     VALUES ('6','Sahara ','3','1')""")                     

db_cursor.execute("""INSERT INTO neighborhoods (ID,NAME)
                     VALUES ('5','Friedrichschain')""")

db_cursor.execute("""INSERT INTO restaurants
                     VALUES ('7','Arirang','5','2')""") 
db_cursor.execute("""INSERT INTO restaurants
                     VALUES ('8','Five Guys','5','3')""") 
db_cursor.execute("""INSERT INTO restaurants
                     VALUES ('9','Nils','5','1')""") 

db_cursor.execute("""CREATE TABLE people(
                     ID integer PRIMARY KEY,
                     NAME text NOT NULL,
                     restaurant_ID integer KEY
                     );""" )

db_cursor.execute("""INSERT INTO people
                     VALUES ('1','Adam','1')""")
db_cursor.execute("""INSERT INTO people
                     VALUES ('2','Soyoon','8')""")
                     
#show restaurants in Xberg 
db_cursor.execute("""SELECT restaurants.NAME, neighborhoods.NAME 
                     FROM restaurants
                     INNER JOIN neighborhoods ON neighborhoods.ID = restaurants.neighborhood_id
                     WHERE neighborhoods.name = 'Kreuzberg'""")

#db_cursor.execute("""SELECT * FROM people
#                     INNER JOIN restaurants ON restaurants.ID = people.restaurant_ID""")


# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()

print("list_restaurants contents:")
print("""
      <html>
      <body>
      list_restaurants)

db_connection.close()
